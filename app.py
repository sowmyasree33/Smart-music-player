import streamlit as st
import cv2
import base64
#import matplotlib.pyplot as plt
#from deepface import DeepFace
import spotipy
from fer import FER
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import test
import random
import vlc
from PIL import Image
#font

img=Image.open('./images/si.png')
st.set_page_config(
    page_title="ADSC",
    page_icon=img
)
st.image('./images/bg.jpeg')
# option = st.selectbox(
#     'Select any one from below',
#     ('automood','mood-selector'))
streamlit_style = """
			<style>
            @import url('https://fonts.googleapis.com/css2?family=Rancho&display=swap');
			html, body, [class*="css"]  {
            font-family: 'Rancho', cursive;
			font-size:1.5rem;
            }
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('./images/mainbackground.png')    
    

option1=0
emotion_detector = FER(mtcnn=True)

client_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager =client_credentials_manager)

header  = st.container()
inp = st.container()
pred = st.container()
st.write("Select any one from the following")
b=st.checkbox('automood-selector')
a=st.checkbox('mood-selector')
f=0
c=0
if a:
    #st.write('You selected:', )
    
    option1 = st.selectbox(
    'How are you feeling?',
    ('select','angry', 'happy', 'sad','neutral','surprise'))
    st.write('You selected:',option1)
    f=1
    if option1=='select':
        c=1
#elif option=='mood-selector':

# if a:
#     happy = st.radio('Happy')
#     sad=st.radio('Sad')
#     angry=st.radio('Angry')
#     neutral=st.radio('Neutral')
#     high=st.radio('High')

#     # if happy:
#     #     option1='happy'
#     # elif sad:
#     #     option1='sad'
#     # elif angry:
#     #     option1='angry'
#     # elif neutral:
#     #     option1='neutral'
#     # elif high:
#     #     option1='high'
#     f=1

if b:
    with header:
       
        st.title('Emotion Detection and Song Recommendation')
        st.markdown('**Aim : To detect the emotion of the person and predict a song**')

    with inp:
        count=1
        st.title("Image Capture")
        st.markdown("**Capturing an image of your face**")
        #faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        test.take_input(count)
        
     
    with pred:
        st.title("Let's see what songs you should listen to !!")
        test_img_low_quality = cv2.imread('./images/photo.png')
        analysis = emotion_detector.detect_emotions(test_img_low_quality)
        print(analysis)
        dominant_emotion, emotion_score = emotion_detector.top_emotion(test_img_low_quality)
        #print(dominant_emotion, emotion_score)

       # plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

        #predictions = DeepFace.analyze(img)
        option1=dominant_emotion
        f=1

    #st.text("Your emotion is {}".format(predictions['dominant_emotion']))  
    #print(predictions['dominant_emotion'])
if c!=1:
    if f==1:
        if(option1 == 'happy'):
            print("Happy emotion detected.")
            add_bg_from_local('./images/happy.png')    
            st.markdown("**You are happy!!**")
            playlist_id = '37i9dQZF1DX6XE7HRLM75P'
        elif(option1== 'sad') :
            print("Sad emotion detected.")
            add_bg_from_local('./images/s.jpg')    
            st.markdown("**You don't look too cheerful....Here are some songs to lift your mood up!!**")
            playlist_id = '3p2tAkOvJqOPYjttRxEQD5'
        elif(option1== 'angry') :
            print("Angry emotion detected.")
            add_bg_from_local('./images/a.jpg')    
            st.markdown("**Angry!!**")
            playlist_id = '3fmrpuOdcxwyoL0zYD7VEr'
        elif(option1== 'surprise') :
            print("Surprise emotion detected.")
            add_bg_from_local('./images/s.jpeg')    
            st.markdown("**surprise!!**")
            playlist_id = '37i9dQZF1DX6XE7HRLM75P'
        elif(option1=='neutral'):
            st.markdown("neutral emotion detected!!")                        
            add_bg_from_local('./images/n.png')    
            playlist_id = '37i9dQZF1DX2UT3NuRgcHd'





        def get_track_ids(playlist_id):
            music_id_list = []
            playlist = sp.playlist(playlist_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list 
        track_ids = get_track_ids(playlist_id)


        for i in range(5):

            random.shuffle(track_ids)

            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html=True)

        # track_ids = ['9g2tgsYDUnE','hYFzyK9ExuM','NCtr6zKDoX4','NwMaEv8qpOk']
        # str1='https://www.youtube.com/embed/'
        
        # for i in range(2):
        #     s=str1+track_ids[i]+'?autoplay=1'

            #random.shuffle(track_ids)
        #my_html='<iframe src="https://www.youtube.com/embed/9g2tgsYDUnE?autoplay=1&mute=1&list=RDCLAK5uy_lyVnWI5JnuwKJiuE-n1x-Un0mj9WlEyZw&loop=1" type="audio/mp3" allow="autoplay" id="audio" style="display:none"></iframe><audio autoplay><source src="https://www.youtube.com/embed/9g2tgsYDUnE?autoplay=1&mute=1&list=RDCLAK5uy_lyVnWI5JnuwKJiuE-n1x-Un0mj9WlEyZw&loop=1" type="audio/mp3"></audio>'
            
            #my_html = '<iframe style="border-radius:12px"  width="100%" height="352" frameBorder="0" allowfullscreen src="https://www.youtube.com/embed/9g2tgsYDUnE?autoplay=1&mute=1&list=RDCLAK5uy_lyVnWI5JnuwKJiuE-n1x-Un0mj9WlEyZw&loop=1"></iframe>'
                
            # st.markdown(my_html, unsafe_allow_html=True)
                #my_html = '<iframe width="560" height="315" src={s}  frameborder="0"></iframe>'

            #st.markdown(my_html, unsafe_allow_html=True)
        #p = vlc.MediaPlayer("https://open.spotify.com/embed/track/{}".format(track_ids[0]))      
        #p.play()
else:     
    st.write("select emotion")
            

        

