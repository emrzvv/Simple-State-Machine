import logging
from keyboards import *
from telegram.ext import ConversationHandler

START, STAGE_1, STAGE_2_1,  STAGE_2_2, STAGE_3_1, STAGE_3_2, STAGE_3_3, STAGE_4 = range(8)

 
def start(bot, update):
    logging.info('[NEW USER UPDATE INFO]: %s', update)
    print(type(START))
    update.message.reply_text("Hello! Here is the 'START' location.", reply_markup=get_start_keyboard())
    return START
 
def stage_1(bot, update):
    update.message.reply_text("Welcome to the Stage 1! Let's go futher. What variant do you choose?",
        reply_markup=get_stage_1_keyboard())
 
    return STAGE_1
 
def stage_2_1(bot, update):
    update.message.reply_text("Stage 2.1? Nice choice! What's next?",
        reply_markup=get_stage_2_1_keyboard())
 
    return STAGE_2_1
 
def stage_2_2(bot, update):
    update.message.reply_text("Stage 2.2? Not so bad. Let's go to the next stage!",
        reply_markup=get_stage_2_2_keyboard())
 
    return STAGE_2_2
 
def stage_3_1(bot, update):
    update.message.reply_text("Oh. Stage 3.1 was wrong choice. Go back to the Stage 1",
        reply_markup=get_stage_3_1_keyboard())
 
    return STAGE_3_1
 
def stage_3_2(bot, update):
    update.message.reply_text("Stage 3.2! You made the right choice!",
        reply_markup=get_stage_3_2_keyboard())
 
    return STAGE_3_2

def stage_3_3(bot, update):
    update.message.reply_text("Stage 3.3! Nice You've almost finished it!",
        reply_markup=get_stage_3_2_keyboard())

    return STAGE_3_3

def stage_4(bot, update):
    update.message.reply_text("Stage 4! Congratulations! Now you can restart the state. :)",
        reply_markup=get_reset_keyboard())
 
    return STAGE_4
 
def reset(bot, update):
    update.message.reply_text("Okay, resetting the state machine.",
        reply_markup=get_start_keyboard())
 
    return START
 
def default_response(bot, update):
    update.message.reply_text("I don't understand you. Try to reset the state.")
 
def done(bot, update):
    update.message.reply_text("Bye-bye. See you later!")
 
    return ConversationHandler.END
    
