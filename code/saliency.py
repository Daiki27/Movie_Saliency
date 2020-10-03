# pip3 install opencv-python --user
# pip3 install opencv-contrib-python --user <= cv2.saliencyを使うために.

# 古典的なサリーエンシー検出を行う.
# input ：mp4動画
# putput：mp4動画：オリジナル＋サリエンシーヒートマップ

import cv2

#Videoを読み込む.
video      = cv2.VideoCapture("video/208.mp4")

#映像情報を取得する.
Width    = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
Height   = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
FrameNum = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
FPS      = int(video.get(cv2.CAP_PROP_FPS))
print(Width, FrameNum)

#出力ファイルの形式を指定.
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

#アルゴリズムの選択.
mode = "SR"
saliency = None
if mode == 'SR':
    saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
elif mode == 'FG':
    saliency = cv2.saliency.StaticSaliencyFineGrained_create()
if saliency is None:
    exit()

#output file name, encoder, fps, size(fit to image size)
path_saliency  = "video/saliency_map.mp4"
video_saliency = cv2.VideoWriter(path_saliency, fourcc, FPS, (Width, Height), False)

path_heatmap   = "video/Heat_map.mp4"
video_heatmap  = cv2.VideoWriter(path_heatmap, fourcc, FPS, (Width, Height), True)

path_result    = "video/Result.mp4"
video_result   = cv2.VideoWriter(path_result, fourcc, FPS, (Width, Height), True)
n = 0
while True:
  ret, frame = video.read()
  if ret:
    (success, saliencyMap) = saliency.computeSaliency(frame)
    saliencyMap = (saliencyMap * 255).astype("uint8")
    video_saliency.write(saliencyMap)
    HeatMap = cv2.applyColorMap(saliencyMap, cv2.COLORMAP_JET)
    video_heatmap.write(HeatMap)
    dst = cv2.addWeighted(frame, 0.5, HeatMap, 0.5, 0)
    video_result.write(dst)
    n = n + 1
  else:
    break;

# release memory.
video.release()
video_saliency.release()
video_heatmap.release()
video_result.release()
