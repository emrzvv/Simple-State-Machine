from telegram import ReplyKeyboardMarkup

def get_start_keyboard():
    keyboard = [['Go to the Stage 1']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
 
def get_reset_keyboard():
    keyboard = [['Reset the state']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
 
def get_stage_1_keyboard():
    keyboard = [['Go to the Stage 2.1','Go to the Stage 2.2'], ['Reset the state']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
 
def get_stage_2_1_keyboard():
    keyboard = [['Go to the Stage 3.1','Go to the Stage 3.2'], ['Reset the state']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
 
def get_stage_2_2_keyboard():  
    keyboard = [['Go to the Stage 3.3'], ['Reset the state']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
 
def get_stage_3_1_keyboard():
    keyboard = [['Go to the Stage 1'], ['Reset the state']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
 
def get_stage_3_2_keyboard():
    keyboard = [['Go to the Stage 4'], ['Reset the state']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    