from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, RegexHandler, Filters
import replies

from config import SAVE_PERIOD

def get_conversation_handler():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', replies.start)],
        states={
            replies.START: [RegexHandler(u'^Go to the Stage 1$', replies.stage_1),
                            MessageHandler(Filters.text, replies.default_response)],

            replies.STAGE_1: [RegexHandler(u'^Go to the Stage 2\.1$', replies.stage_2_1),
                              RegexHandler(u'^Go to the Stage 2\.2$', replies.stage_2_2),
                              RegexHandler(u'^Reset the state$', replies.reset),
                              MessageHandler(Filters.text, replies.default_response)],

            replies.STAGE_2_1: [RegexHandler(u'^Go to the Stage 3\.1$', replies.stage_3_1),
                                RegexHandler(u'^Go to the Stage 3\.2$', replies.stage_3_2),
                                RegexHandler(u'^Reset the state$', replies.reset),
                                MessageHandler(Filters.text, replies.default_response)],

            replies.STAGE_2_2: [RegexHandler(u'^Go to the Stage 3\.3$', replies.stage_3_3),
                                RegexHandler(u'^Reset the state$', replies.reset),
                                MessageHandler(Filters.text, replies.default_response)],
            
            replies.STAGE_3_1: [RegexHandler(u'^Go to the Stage 1$', replies.stage_1),
                                RegexHandler(u'^Reset the state$', replies.reset),
                                MessageHandler(Filters.text, replies.default_response)],

            replies.STAGE_3_2: [RegexHandler(u'^Go to the Stage 4$', replies.stage_4),
                                RegexHandler(u'^Reset the state$', replies.start),
                                MessageHandler(Filters.text, replies.default_response)],

            replies.STAGE_3_3: [RegexHandler(u'^Go to the Stage 4$', replies.stage_4),
                                RegexHandler(u'^Reset the state$', replies.start),
                                MessageHandler(Filters.text, replies.default_response)],

            replies.STAGE_4: [RegexHandler(u'^Reset the state$', replies.reset),
                              MessageHandler(Filters.text, replies.default_response)]
        },
        fallbacks=[CommandHandler('cancel', replies.done)],
        allow_reentry=True
    )

    return conv_handler


