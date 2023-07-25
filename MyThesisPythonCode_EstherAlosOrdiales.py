# set language to python




# import os > to provide a way to interact with the operating system 
import os
# import the module to be able to select random elements (for randomizing the transcription participants)
import random
# import other necessary libraries
import pandas
import textgrid
import praatIO
import parselmouth
import wave
import pandas as pd
import speech_recognition as sr
import sklearn 
import numpy as np
import sklearn 


# change working directory > os.chdir("...")
os.chdir("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio")
# import the library that facilitates the automatic transcription process, then set it with an abreviation
import speech_recognition as sr
# identify the folder where the audio files are, so they can be randomized
adresso_audio_files_training_controls = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/cn"
# generate a list from the files in the folder
controls_list = os.listdir(adresso_audio_files_training_controls)
# confirm the list
#controls_list
# generate a random selection of 20 participants (controls)
## random_controls_list = random.sample(controls_list, 20)
# confirm the random selection of 20 controls from the training data, after ordering it in ascending order
# random_controls_list = sorted(random_controls_list)
# print(random_controls_list)
# mark the files you want to transcribe. In this case, it is the randomized list of control participants
recognizer = sr.Recognizer()
#ran_control_audio_files = [random_controls_list]

'''
# to run an individual file, this would be the code to be used:

audio_control_289 = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/cn/adrso289.wav" #it is important to add the .wav file extension
with sr.AudioFile(audio_control_289) as source:
    audio = recognizer.record(source)
    try:
        transcription_audio = recognizer.recognize_google(audio)
        print(f"Transcription: {transcription_audio}")
    except sr.RequestError as e:
        print(f"Error: {e}")
    except:
        print("Speech recognition could not understand audio") 

'''

'''
# run the transcription the files in a loop, meaning it will run the command to recognize the speech individually in ALL samples of the control audios until finished

audios_trainingdata_controls = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/cn" 
audio_files = os.listdir(audios_trainingdata_controls)

for audio_file in audio_files:
    audio_path = os.path.join(audios_trainingdata_controls, audio_file)
    
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        
        try: 
            transcription = recognizer.recognize_google(audio) 
            print(f"Transcription for {audio_file}: {transcription}")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.UnknownValueError:
            print(f"Unable to transcribe {audio_file}")

'''


# instead of running the code to transcribe the whole list of control audios, here is a loop to run the randomly generated list of 20 controls. 
# Once the list is generated, I will use the same files for further analysis.

audios_trainingdata_controls = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/cn" 
audio_files = os.listdir(audios_trainingdata_controls)
'''
for audio_file in random_controls_list:
    audio_path = os.path.join(audios_trainingdata_controls, audio_file)
    
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        
        try: 
            transcription = recognizer.recognize_google(audio) 
            print(f"Transcription for {audio_file}: {transcription}")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.UnknownValueError:
            print(f"Unable to transcribe {audio_file}")

'''

# then, the same process applies for the training audios for patients with Alzheimer's disease (ad)
# first, mark the directory and identify the folder with the training data and the patients with ad
# then, the transcript code for one of the patient audios
# then, the transcript code for ALL the audios for the patients
# and finally, the transcript code for the randomly generated list of patient audios 

# identify the folder where the audio files are, so they can be randomized
adresso_audio_files_training_patients = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/ad"
# generate a list from the files in the folder
patients_list = os.listdir(adresso_audio_files_training_patients)
# confirm the list
# patients_list
# generate a random selection of 20 participants (patients)
# random_patients_list = random.sample(patients_list, 20)
# confirm the random selection of 20 controls from the training data, after ordering it in ascending order
#random_patients_list = sorted(random_patients_list)
# print(random_patients_list)
# mark the files you want to transcribe. In this case, it is the randomized list of control participants
recognizer = sr.Recognizer()
#ran_patient_audio_files = [random_patients_list]


'''
# to run an individual file, this would be the code to be used:

audio_patient_125 = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/ad/adrso125.wav" #it is important to add the .wav file extension
with sr.AudioFile(audio_patient_125) as source:
    audio = recognizer.record(source)
    try:
        transcription_audio = recognizer.recognize_google(audio)
        print(f"Transcription: {transcription_audio}")
    except sr.RequestError as e:
        print(f"Error: {e}")
    except:
        print("Speech recognition could not understand audio") 

'''
# the script seemed to have problems with some of the audio files, so I created a subcode to detect which files were corrupted

import wave
'''
def find_corrupted_audio_files(audios_trainingdata_patients):
    corrupted_files = []

    for file_name in os.listdir(audios_trainingdata_patients):
        file_path = os.path.join(audios_trainingdata_patients, file_name)
        try:
            with wave.open(file_path, 'rb') as audio_file:
                # Check if the audio file can be read successfully
                pass
        except wave.Error:
            corrupted_files.append(file_name)

    return corrupted_files

'''

# corrupted_files_list = find_corrupted_audio_files("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/ad" )
print("Corrupted files:")
# print(corrupted_files_list)


'''
# run the transcription the files in a loop, meaning it will run the command to recognize the speech individually in ALL samples of the random patients audio until finished,
# excluding the corrupted files


audios_trainingdata_patients = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/ad" 
audio_files2 = os.listdir(audios_trainingdata_patients)


for audio_file in audio_files2:
    audio_path = os.path.join(audios_trainingdata_patients, audio_file)
    if audio_file in corrupted_files_list:
        continue
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        
        try: 
            transcription = recognizer.recognize_google(audio) 
            print(f"Transcription for {audio_file}: {transcription}")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.UnknownValueError:
            print(f"Unable to transcribe {audio_file}")
'''

'''

# instead of running the code to transcribe the whole list of PATIENTS WITH AD audios, here is a loop to run the randomly generated list of 20 patients with AD. 
# once the list is generated, I will use the same files for further analysis.
# for this loop too I had to include the list of corrupted files, so they would not be in the randomized list

audios_trainingdata_patients = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/ad" 
audio_files2 = os.listdir(audios_trainingdata_patients)

for audio_file in random_patients_list:
    audio_path = os.path.join(audios_trainingdata_patients, audio_file)
    
    if audio_file in corrupted_files_list:
        continue
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        
        try: 
            transcription = recognizer.recognize_google(audio) 
            print(f"Transcription for {audio_file}: {transcription}")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.UnknownValueError:
            print(f"Unable to transcribe {audio_file}")

'''





# then, the same process applies for the testing audios in the dataset
# first, mark the directory and identify the folder with the testing data 
# then, the transcript code for one of the testing audios
# then, the transcript code for ALL the audios for the testing data
# and finally, the transcript code for the randomly generated list of testing audios 

# identify the folder where the audio files are, so they can be randomized
adresso_audio_files_testing = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/test/diagnosis/test-dist/audio"
# generate a list from the files in the folder
testing_list = os.listdir(adresso_audio_files_testing)
# confirm the list
# testing_list
# generate a random selection of 20 testing audios
# random_testing_list = random.sample(testing_list, 20)
# confirm the random selection of 20 controls from the testing data, after ordering it in ascending order
# random_testing_list = sorted(random_testing_list)
# print(random_testing_list)
# mark the files you want to transcribe. In this case, it is the randomized list of testing audios
recognizer = sr.Recognizer()
# ran_testing_audio_files = [random_testing_list]


'''
# to run an individual file, this would be the code to be used:

audio_testing_19 = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/test/diagnosis/test-dist/audio/adrsdt19.wav" #it is important to add the .wav file extension
with sr.AudioFile(audio_testing_19) as source:
    audio = recognizer.record(source)
    try:
        transcription_audio = recognizer.recognize_google(audio)
        print(f"Transcription: {transcription_audio}")
    except sr.RequestError as e:
        print(f"Error: {e}")
    except:
        print("Speech recognition could not understand audio") 

'''
# the script seemed to have problems with some of the audio files, so I created a subcode to detect which files were corrupted
import wave

def find_corrupted_audio_files(audios_trainingdata_patients):
    corrupted_files = []

    for file_name in os.listdir(audios_trainingdata_patients):
        file_path = os.path.join(audios_trainingdata_patients, file_name)
        try:
            with wave.open(file_path, 'rb') as audio_file:
                # Check if the audio file can be read successfully
                pass
        except wave.Error:
            corrupted_files.append(file_name)

    return corrupted_files



corrupted_files_list = find_corrupted_audio_files("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/train/audio/ad" )
print("Corrupted files:")
print(corrupted_files_list)


'''
# run the transcription the files in a loop, meaning it will run the command to recognize the speech individually in ALL samples of the random testing audio until finished

audios_testingdata = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/test/diagnosis/test-dist/audio" 

audio_files3 = os.listdir(audios_testingdata)
audio_files3 = sorted(audio_files3)

for audio_file in audio_files3:
    audio_path = os.path.join(audios_testingdata, audio_file)
    #if audio_file in corrupted_files_list:
     #   continue
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        
        try: 
            transcription = recognizer.recognize_google(audio) 
            print(f"Transcription for {audio_file}: {transcription}")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.UnknownValueError:
            print(f"Unable to transcribe {audio_file}")
'''

'''

# instead of running the code to transcribe the whole list of TESTING audios, here is a loop to run the randomly generated list of 20 testing audios. 
# Once the list is generated, I will use the same files for further analysis.
# for this loop too I had to include the list of corrupted files, so they would not be in the randomized list

audios_testingdata = "C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/test/diagnosis/test-dist/audio" 
audio_files3 = os.listdir(audios_testingdata)
audio_files = sorted(audio_files3)

for audio_file in random_testing_list:
    audio_path = os.path.join(audios_testingdata, audio_file)
    
    if audio_file in corrupted_files_list:
        continue
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        
        try: 
            transcription = recognizer.recognize_google(audio) 
            print(f"Transcription for {audio_file}: {transcription}")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.UnknownValueError:
            print(f"Unable to transcribe {audio_file}")

'''

# all ran_control_audio_files = ['adrso003.wav', 'adrso005.wav', 'adrso010.wav', 'adrso017.wav', 'adrso018.wav', 'adrso021.wav', 'adrso153.wav', 'adrso161.wav', 'adrso168.wav', 'adrso180.wav', 'adrso257.wav', 'adrso260.wav', 'adrso266.wav', 'adrso267.wav', 'adrso273.wav', 'adrso276.wav', 'adrso285.wav', 'adrso298.wav', 'adrso302.wav', 'adrso316.wav']
# the simplified list with labeled transcriptions
ran_control_audio_files = ['adrso003.wav', 'adrso005.wav', 'adrso010.wav']

# all ran_patient_audio_files= ['adrso024.wav', 'adrso046.wav', 'adrso047.wav', 'adrso055.wav', 'adrso059.wav', 'adrso060.wav', 'adrso077.wav', 'adrso078.wav', 'adrso089.wav', 'adrso122.wav', 'adrso123.wav', 'adrso189.wav', 'adrso198.wav', 'adrso205.wav', 'adrso212.wav', 'adrso228.wav', 'adrso229.wav', 'adrso233.wav', 'adrso246.wav', 'adrso253.wav']
# the simplified list with labeled transcriptions 
ran_patient_audio_files= ['adrso024.wav', 'adrso046.wav']

# all ran_testing_audio_files = ['adrsdt15.wav', 'adrsdt23.wav', 'adrsdt24.wav', 'adrsdt25.wav', 'adrsdt27.wav', 'adrsdt36.wav', 'adrsdt38.wav', 'adrsdt42.wav', 'adrsdt43.wav', 'adrsdt44.wav', 'adrsdt45.wav', 'adrsdt48.wav', 'adrsdt49.wav', 'adrsdt5.wav', 'adrsdt56.wav', 'adrsdt58.wav', 'adrsdt6.wav', 'adrsdt61.wav', 'adrsdt63.wav', 'adrsdt66.wav']
# simplified list with labeled transcriptions
ran_testing_audio_files = ['adrsdt15.wav', 'adrsdt23.wav']


print (ran_control_audio_files)
print (ran_patient_audio_files)
print (ran_testing_audio_files)


# Importing Pandas to create DataFrame
import pandas as pd
# Importing the relevant package for the program to understand TextGrid Praat files
from praatio import textgrid


# Define the tier names and their respective subcategories
praat_tiers = ['UtteranceText', 'ParaphasicErrors', 'GrammaticalErrors', 'Hesitation', 'Filler', 'Repetitions', 'EmptySpeech', 'DiscourseMarkers', 'OtherActions']
subcategories = {
    'ParaphasicErrors': ['PE_SP', 'PE_PP'],
    'GrammaticalErrors': ['GE_T', 'GE_PR', 'GE_WO', 'GE_O'],
    'Hesitation': ['HES_PAU', 'HES_SI'],
    'Filler': ['FW_WFD', 'FW_F', 'FW_C'],
    'Repetitions': ['REP_SWO', 'REP_WO', 'REP_PHR'],
    'EmptySpeech': ['ES'],
    'DiscourseMarkers': ['DM_T', 'DM_O'],
    'OtherActions': ['OA_REV', 'OA_REF', 'INT', 'OA_CTU_S1', 'OA_CTU_S2', 'OA_CTU_S3', 'OA_CTU_L1', 'OA_CTU_L2', 'OA_CTU_O1',
                     'OA_CTU_O2', 'OA_CTU_O3', 'OA_CTU_O4', 'OA_CTU_O5', 'OA_CTU_O6', 'OA_CTU_O7', 'OA_CTU_O8', 'OA_CTU_O9',
                     'OA_CTU_O10', 'OA_CTU_O11', 'OA_CTU_O12', 'OA_CTU_A1', 'OA_CTU_A2', 'OA_CTU_A3', 'OA_CTU_A4', 'OA_CTU_A5',
                     'OA_CTU_A6', 'OA_CTU_A7']
}

PE_SP = "ParaphasicErrors_SemanticParaphasia"
PE_PP = "ParaphasicErrors_PhonologicalParaphasia"
GE_T = "GrammaticalErrors_Tense"
GE_PR = "GrammaticalErrors_Pronoun"
GE_WO = "GrammaticalError_WordOrder"
GE_O = "GrammaticalError_Other"
HES_PAU = "Hesitation_Pause"
HES_SI = "Hesitation_Silence"
FW_WFD = "FillerWord_WordFindingDifficulties"
FW_C = "FillerWord_Connective"
FW_F = "FillerWord_Filler"
REP_SWO = "Repetition_SubWord"
REP_WO = "Repetition_Word"
REP_PHR = "Repetition_Phrase"
EP = "EmptySpeech"
DM_T = "DiscourseMarker_TemporalCohesion"
DM_O = "DiscourseMarker_OtherCohesion"
INT = "Intended"
OA_REV = "OtherActions_Revision"
OA_REF = "OtherActions_Reformulation"
OA_CTU_S1 = "OtherActions_CookieTheftUnits_Subject1_Boy/Son"
OA_CTU_S2 = "OtherActions_CookieTheftUnits_Subject2_Girl/Daughter"
OA_CTU_S3 = "OtherActions_CookieTheftUnits_Subject3_Mother/Woman"
OA_CTU_L1 = "OtherActions_CookieTheftUnits_Location1_Kitchen"
OA_CTU_L2 = "OtherActions_CookieTheftUnits_Location2_Garden"
OA_CTU_O1 = "OtherActions_CookieTheftUnits_Object1_Cabinet/Cupboard"
OA_CTU_O2 = "OtherActions_CookieTheftUnits_Object2_Cookies"
OA_CTU_O3 = "OtherActions_CookieTheftUnits_Object3_Counter"
OA_CTU_O4 = "OtherActions_CookieTheftUnits_Object4_Curtain"
OA_CTU_O5 = "OtherActions_CookieTheftUnits_Object5_Dishes"
OA_CTU_O6 = "OtherActions_CookieTheftUnits_Object6_Faucet"
OA_CTU_O7 = "OtherActions_CookieTheftUnits_Object7_Floor/Ground"
OA_CTU_O8 = "OtherActions_CookieTheftUnits_Object8_Jar"
OA_CTU_O9 = "OtherActions_CookieTheftUnits_Object9_Plate(s)"
OA_CTU_O10 = "OtherActions_CookieTheftUnits_Object10_Sink"
OA_CTU_O11= "OtherActions_CookieTheftUnits_Object11_Stool"
OA_CTU_O12= "OtherActions_CookieTheftUnits_Object12_Window"

# Load the annotatedTextGrid files

tg_cn_003 = textgrid.openTextgrid("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/cn_adrso003.TextGrid", includeEmptyIntervals=True)
tg_cn_005 = textgrid.openTextgrid("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/cn_adrso005.TextGrid", includeEmptyIntervals=True)
tg_cn_010 = textgrid.openTextgrid("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/cn_adrso010.TextGrid", includeEmptyIntervals=True)
tg_ad_024 = textgrid.openTextgrid("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/ad_adrso024.TextGrid", includeEmptyIntervals=True)
tg_ad_046 = textgrid.openTextgrid("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/ad_adrso046.TextGrid", includeEmptyIntervals=True)
tg_test_015 = textgrid.openTextgrid("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/test_adrsdt15.TextGrid", includeEmptyIntervals=True)
tg_test_023 = textgrid.openTextgrid("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/test_adrsdt23.TextGrid", includeEmptyIntervals=True)


# This code prints out the number of instances in each tier. However, this is data saved only within the loop itself. For the saved data, proceed to the next section
# For control 003
for tier_name in praat_tiers:
    tier = tg_cn_003._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    instances = 0
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                instances += 1
        print(f"Instances: {instances}")
    else:
        instances = 0
        print(f"Instances: {instances}")

# For control 005
for tier_name in praat_tiers:
    tier = tg_cn_005._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    instances = 0
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                instances += 1
        print(f"Instances: {instances}")
    else:
        instances = 0
        print(f"Instances: {instances}")

# For control 010
for tier_name in praat_tiers:
    tier = tg_cn_010._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    instances = 0
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                instances += 1
        print(f"Instances: {instances}")
    else:
        instances = 0
        print(f"Instances: {instances}")

# For patient 024
for tier_name in praat_tiers:
    tier = tg_ad_024._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    instances = 0
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                instances += 1
        print(f"Instances: {instances}")
    else:
        instances = 0
        print(f"Instances: {instances}")



# For patient 046
for tier_name in praat_tiers:
    tier = tg_ad_046._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    instances = 0
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                instances += 1
        print(f"Instances: {instances}")
    else:
        instances = 0
        print(f"Instances: {instances}")

# For test 015
for tier_name in praat_tiers:
    tier = tg_test_015._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    instances = 0
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                instances += 1
        print(f"Instances: {instances}")
    else:
        instances = 0
        print(f"Instances: {instances}")

# For test 023
for tier_name in praat_tiers:
    tier = tg_test_023._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    instances = 0
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                instances += 1
        print(f"Instances: {instances}")
    else:
        instances = 0
        print(f"Instances: {instances}")
        


# This section prints out the annotations in their respective tiers, for each textgrid individually. Here is where my transcriptions have been printed too. This data can be included in a table with the insert function (that will insert the list of labels)

# For control 003
labels_cn003 = []
for tier_name in praat_tiers:
    tier = tg_cn_003._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    labellist_cn003 = []
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                labellist_cn003.append(interval.label)
        print(f"Instances: {labellist_cn003}")
    else:
        instances = 0
        print(f"Instances: {labellist_cn003}")
    labels_cn003.append(labellist_cn003)


# For control 005
labels_cn005 = []
for tier_name in praat_tiers:
    tier = tg_cn_005._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    labellist_cn005 = []
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                labellist_cn005.append(interval.label)
        print(f"Instances: {labellist_cn005}")
    else:
        instances = 0
        print(f"Instances: {labellist_cn005}")
    labels_cn005.append(labellist_cn005)
    
# For control 010
labels_cn010 = []
for tier_name in praat_tiers:
    tier = tg_cn_010._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    labellist_cn010 = []
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                labellist_cn010.append(interval.label)
        print(f"Instances: {labellist_cn010}")
    else:
        instances = 0
        print(f"Instances: {labellist_cn010}")
    labels_cn010.append(labellist_cn010)
    
    
# For patient 024
labels_ad024 = []
for tier_name in praat_tiers:
    tier = tg_ad_024._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    labellist_ad024 = []
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                labellist_ad024.append(interval.label)
        print(f"Instances: {labellist_ad024}")
    else:
        instances = 0
        print(f"Instances: {labellist_ad024}")
    labels_ad024.append(labellist_ad024)


# For patient 046
labels_ad046 = []
for tier_name in praat_tiers:
    tier = tg_ad_046._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    labellist_ad046 = []
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                labellist_ad046.append(interval.label)
        print(f"Instances: {labellist_ad046}")
    else:
        instances = 0
        print(f"Instances: {labellist_ad046}")
    labels_ad046.append(labellist_ad046)

# For test 015
labels_test015 = []
for tier_name in praat_tiers:
    tier = tg_test_015._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    labellist_test015 = []
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                labellist_test015.append(interval.label)
        print(f"Instances: {labellist_test015}")
    else:
        instances = 0
        print(f"Instances: {labellist_test015}")
    labels_test015.append(labellist_test015)
    
# For test 23
labels_test023 = []
for tier_name in praat_tiers:
    tier = tg_test_023._tierDict.get(tier_name)
    
    print(f"Tier: {tier_name}")
    
    labellist_test023 = []
    if tier:
        for interval in tier.entries:
            if interval.label != '':
                labellist_test023.append(interval.label)
        print(f"Instances: {labellist_test023}")
    else:
        instances = 0
        print(f"Instances: {labellist_test023}")
    labels_test023.append(labellist_test023)



# The tables with the data are created in this section

# Creating Empty DataFrame and Storing it in variable df. This is the code blueprint
df = pd.DataFrame({}, index=praat_tiers)
  
# Printing Empty DataFrame to test it
df
  
# Creating the link to the data previously obtained. This will print the subcategories present in each textgrid
df.insert(0,"Labels_cn003",labels_cn003, True)
df.insert(0,"Labels_cn005",labels_cn005, True)
df.insert(0,"Labels_cn010",labels_cn010, True)
df.insert(0,"Labels_ad024",labels_ad024, True)
df.insert(0,"Labels_ad046",labels_ad046, True)
df.insert(0,"Labels_test015",labels_test015, True)
df.insert(0,"Labels_test023",labels_test023, True)

# Adding a row with the count of each subcategory in each textgrid
df['Count_cn003'] = [len(c) for c in df['Labels_cn003']]
df['Count_cn005'] = [len(c) for c in df['Labels_cn005']]
df['Count_cn010'] = [len(c) for c in df['Labels_cn010']]
df['Count_ad024'] = [len(c) for c in df['Labels_ad024']]
df['Count_ad046'] = [len(c) for c in df['Labels_ad046']]
df['Count_test015'] = [len(c) for c in df['Labels_test015']]
df['Count_test023'] = [len(c) for c in df['Labels_test023']]


# EXPLAIN 
Ad_noAd = {"Count_cn003":0, "Count_cn005":0, "Count_cn010":0, "Count_ad024":1, "Count_ad046":1}
# Use the loc method to add the new row to the DataFrame
df = df.append(pd.Series(Ad_noAd, index=df.columns, name='Ad_noAd'))
# Display the modified DataFrame
print(df)


# Printing the table and Exporting the table in a cvs file 
# Table for all data. File output is cvs with name: TiersSubcategories_AllData_PrintAndCount
df_AllData_PrintAndCount =df[["Labels_cn003", "Count_cn003", "Labels_cn005", "Count_cn005", "Labels_cn010", "Count_cn010", "Labels_ad024", "Count_ad024", "Labels_ad046", "Count_ad046", "Labels_test015", "Count_test015", "Labels_test023", "Count_test023"]]
df_AllData_PrintAndCount.to_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/TiersSubcategories_AllData_PrintAndCount.csv")

# Table for training data. File output is cvs with name: TiersSubcategories_TrainingData_PrintAndCount
df_TrainingData_PrintAndCount =df[["Labels_cn003", "Count_cn003", "Labels_cn005", "Count_cn005", "Labels_cn010", "Count_cn010", "Labels_ad024", "Count_ad024", "Labels_ad046", "Count_ad046"]]
df_TrainingData_PrintAndCount.to_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/TiersSubcategories_TrainingData_PrintAndCount.csv")

# Table for testing data. File output is cvs with name: TiersSubcategories_TestingData_PrintAndCount
df_TestingData_PrintAndCount =df[["Labels_test015", "Count_test015", "Labels_test023", "Count_test023"]] 
df_TestingData_PrintAndCount.to_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/TiersSubcategories_TestingData_PrintAndCount.csv")

# Table for all participants and counts in the training dataset. Table for the analysis part. File output is cvs with name: TiersSubcategories_TrainingData_CountforAnalysis
df_TrainingData_CountforAnalysis =df[["Count_cn003", "Count_cn005", "Count_cn010", "Count_ad024", "Count_ad046"]]
df_TrainingData_CountforAnalysis.to_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/TiersSubcategories_TrainingData_CountforAnalysis.csv")

# Table for all participants and counts in the testing dataset. Table for the analysis part. File output is cvs with name: TiersSubcategories_TestingData_CountforAnalysis
df_TestingData_CountforAnalysis =df[["Count_test015", "Count_test023"]]
df_TestingData_CountforAnalysis.to_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/TiersSubcategories_TestingData_CountforAnalysis.csv")

# Table with the Cookie Theft Test results per particpant 
tg_participants = ["cn_adrso003","cn_adrso005","cn_adrso010","ad_adrso024","ad_adrso046","test_adrsdt15","test_adrsdt23"]
content_list = []
for participant in tg_participants:

    textgrid_file = textgrid.openTextgrid(f"C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/Annotations_TextGrids/{participant}.TextGrid", includeEmptyIntervals=True)

    OtherActions_tier = textgrid_file._tierDict.get("OtherActions")

    labellist = []

    if OtherActions_tier:
        for interval in OtherActions_tier.entries:
            if interval.label != '' and "CTU" in interval.label:
                labellist.append(interval.label)
        print(f"Instances: {labellist}")
    content_list.append(len(labellist))

content = {"Cookie Theft Test Result": content_list}
df = pd.DataFrame(content, index=tg_participants)
df.index.name = "Participants"
df.to_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/CookieTheftTest_Results.csv")



# ANALYSIS 
# Descriptive statistics of the counts of subcategories per textgrid
descriptive_statistics = {}

for column in df.columns:
    if column.startswith('Count_'):
        column_name = column.replace('Count_', '')
        descriptive_statistics[column_name] = df[column].describe()[1:]  # Exclude the count row

# Create a DataFrame from the statistics dictionary
table_descriptive_statistics_instances_subcategories = pd.DataFrame(descriptive_statistics)

# Print the table
print(table_descriptive_statistics_instances_subcategories)
table_descriptive_statistics_instances_subcategories.to_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/table_descriptive_statistics_instances_subcategorie.csv")

# Logistic Regression 
 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/TiersSubcategories_TrainingData_CountforAnalysis.csv")


# Separating the features (X) and the labels (y)
X = data.iloc[:-1, 1:].values  # Features: all rows except the last one, all columns starting from the second one
y = data.iloc[-1, 1:].values   # Target variable: last row, all columns starting from the second one
y = y.astype(int)
print(X)
print(y)

# Creating an instance of the LogisticRegression model
LRmodel = LogisticRegression()
X = X.T
LRmodel.fit(X, y)



# Make predictions on the training data
coefficients = LRmodel.coef_[0]
print(coefficients)
y_pred = LRmodel.predict(X)
print(y_pred)


# Now, I take the model, which has worked with the already defined binary outcomes of Ad(1) and noAd(0), and introduce the testing data
test_data = pd.read_csv("C:/Users/eofic/OneDrive/Escritorio/Thesis.DT/DataSet_ADReSSo2021/diagnosis/TiersSubcategories_TestingData_CountforAnalysis.csv")

Xtest = test_data.iloc[:,1:].values.T
Xtest

LRmodel.predict(Xtest)

LRmodel.predict_proba(Xtest)
LRmodel.predict_proba(X)

# Variable importance
from sklearn.inspection import permutation_importance

LRmodel_importance = permutation_importance(LRmodel, X, y)
print (LRmodel_importance)
