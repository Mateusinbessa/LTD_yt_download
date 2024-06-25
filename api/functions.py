from pytube import YouTube
from time import time
import os

def download_audio(url, path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)

        yt = YouTube(url)
        streams = yt.streams.filter(only_audio=True)

        if streams:
            audio_stream = streams[0]
            inicio_download = time()
            audio_stream.download(output_path=path)
            fim_download = time()
            tempo_decorrido = fim_download - inicio_download
            return {'status': 'success', 'message': f"Download do áudio '{yt.title}' concluído em {tempo_decorrido:.2f} segundos."}
        else:
            return {'status': 'error', 'message': "Não foi possível encontrar nenhum stream de áudio disponível."}

    except Exception as e:
        return {'status': 'error', 'message': f"Ocorreu um erro ao baixar o áudio: {str(e)}"}

def download_video(url, path):
        if not os.path.exists(path):
            os.makedirs(path)

        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')

        if streams:
            video_stream = streams.get_highest_resolution()
            try:
                inicio_download = time()
                video_stream.download(output_path=path)
                fim_download = time()
                tempo_decorrido = fim_download - inicio_download
                return {'status': 'success', 'message': f"Download do vídeo '{yt.title}' concluído em {tempo_decorrido:.2f} segundos."}
            except Exception as e:
                return {'status': 'error', 'message': f"Ocorreu um erro ao baixar o vídeo: {str(e)}"}
        else:
            return {'status': 'error', 'message': 'Nenhum stream de vídeo disponível.'}

