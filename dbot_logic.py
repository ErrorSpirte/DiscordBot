import random, requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji():
    emodji = [":grinning:", ":smiley:", ":smile:", ":grin:", ":laughing:", ":sweat_smile:", ":rofl:", ":joy:", ":slight_smile:", ":upside_down:", ":melting_face:", ":wink:", ":blush:", ":innocent:", ":smiling_face_with_3_hearts:", ":heart_eyes:", ":star_struck:", ":kissing_heart:", ":kissing:", ":relaxed:", ":kissing_closed_eyes:", ":kissing_smiling_eyes:", ":smiling_face_with_tear:", ":yum:", ":stuck_out_tongue:", ":stuck_out_tongue_winking_eye:", ":zany_face:", ":stuck_out_tongue_closed_eyes:", ":money_mouth:", ":hugging:", ":face_with_hand_over_mouth:", ":face_with_open_eyes_and_hand_over_mouth:", ":face_with_peeking_eye:", ":shushing_face:", ":thinking:", ":saluting_face:", ":zipper_mouth:", ":face_with_raised_eyebrow:", ":neutral_face:", ":expressionless:", ":no_mouth:", ":dotted_line_face:", ":face_in_clouds:", ":smirk:", ":unamused:", ":rolling_eyes:", ":grimacing:", ":face_exhaling:", ":lying_face:", ":shaking_face:", ":relieved:", ":pensive:", ":sleepy:", ":drooling_face:", ":sleeping:", ":mask:", ":thermometer_face:", ":head_bandage:", ":nauseated_face:", ":face_vomiting:", ":sneezing_face:", ":hot_face:", ":cold_face:", ":woozy_face:", ":dizzy_face:", ":face_with_spiral_eyes:", ":exploding_head:", ":cowboy:", ":partying_face:", ":disguised_face:", ":sunglasses:", ":nerd:", ":face_with_monocle:", ":confused:", ":face_with_diagonal_mouth:", ":worried:", ":slight_frown:", ":frowning2:", ":open_mouth:", ":hushed:", ":astonished:", ":flushed:", ":pleading_face:", ":face_holding_back_tears:", ":frowning:", ":anguished:", ":fearful:", ":cold_sweat:", ":disappointed_relieved:", ":cry:", ":sob:", ":scream:", ":confounded:", ":persevere:", ":disappointed:", ":sweat:", ":weary:", ":tired_face:", ":yawning_face:", ":triumph:", ":rage:", ":angry:", ":face_with_symbols_over_mouth:", ":smiling_imp:", ":imp:", ":skull:", ":skull_crossbones:", ":poop:", ":clown:", ":japanese_ogre:", ":japanese_goblin:", ":ghost:", ":alien:", ":space_invader:", ":robot:", ":smiley_cat:", ":smile_cat:", ":joy_cat:", ":heart_eyes_cat:", ":smirk_cat:", ":kissing_cat:", ":scream_cat:", ":crying_cat_face:", ":pouting_cat:", ":see_no_evil:", ":hear_no_evil:", ":speak_no_evil:", ":kiss:", ":100:", ":anger:", ":boom:", ":dizzy:", ":sweat_drops:", ":dash:", ":hole:", ":zzz:", ":wave:", ":raised_back_of_hand:", ":hand_splayed:", ":raised_hand:", ":vulcan:", ":rightwards_hand:", ":leftwards_hand:", ":palm_down_hand:", ":palm_up_hand:", ":leftwards_pushing_hand:", ":rightwards_pushing_hand:", ":ok_hand:", ":pinched_fingers:", ":pinching_hand:", ":v:", ":fingers_crossed:", ":hand_with_index_finger_and_thumb_crossed:", ":love_you_gesture:", ":metal:", ":call_me:", ":point_left:", ":point_right:", ":point_up_2:", ":point_down:", ":point_up:", ":index_pointing_at_the_viewer:", ":thumbsup:", ":thumbsdown:", ":fist:", ":punch:", ":left_facing_fist:", ":right_facing_fist:", ":clap:", ":raised_hands:", ":heart_hands:", ":open_hands:", ":palms_up_together:", ":handshake:", ":pray:", ":writing_hand:", ":nail_care:", ":selfie:", ":muscle:", ":mechanical_arm:", ":mechanical_leg:", ":leg:", ":foot:", ":ear:", ":ear_with_hearing_aid:", ":nose:", ":brain:", ":anatomical_heart:", ":lungs:", ":tooth:", ":bone:", ":eyes:", ":eye:", ":tongue:", ":lips:", ":love_letter:", ":cupid:", ":gift_heart:", ":sparkling_heart:", ":heartpulse:", ":heartbeat:", ":revolving_hearts:", ":two_hearts:", ":heart_decoration:", ":heart_exclamation:", ":broken_heart:", ":heart_on_fire:", ":mending_heart:", ":speaking_head:", ":radioactive:", ":biohazard:", ":arrow_up:", ":arrow_upper_right:", ":arrow_right:", ":arrow_lower_right:", ":arrow_down:", ":arrow_lower_left:", ":arrow_left:", ":arrow_upper_left:", ":arrow_up_down:", ":left_right_arrow:", ":leftwards_arrow_with_hook:", ":arrow_right_hook:", ":arrow_heading_up:", ":arrow_heading_down:", ":arrows_clockwise:", ":arrows_counterclockwise:", ":back:", ":end:", ":on:", ":soon:", ":top:", ":heavy_multiplication_x:", ":heavy_plus_sign:", ":heavy_minus_sign:", ":heavy_division_sign:", ":heavy_equals_sign:", ":infinity:", ":bangbang:", ":interrobang:", ":question:", ":grey_question:", ":grey_exclamation:", ":exclamation:", ":a:", ":ab:", ":b:", ":cl:", ":cool:", ":free:", ":information_source:", ":id:", ":m:", ":new:", ":ng:", ":o2:", ":ok:", ":parking:", ":sos:", ":up:", ":vs:"]
    return random.choice(emodji)

def magic_ball():
    responses = ["Да", "Нет", "Возможно", "Не знаю"]
    return random.choice(responses)

def get_help():
    return """Доступные команды:
    !hello, !hi, !привет - приветствие
    !bye, !пока - прощание
    !pass, !пароль - генерация пароля
    !emoji - генерация смайлика
    !magic, !магия - магический шар"""

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']