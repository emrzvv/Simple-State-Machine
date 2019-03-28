from config import *
import sys, time, logging, threading, pickle, promise
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from conversation_handler import get_conversation_handler


def set_logging():
    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, filename=LOG_FILE)

    console = logging.StreamHandler()
    console.setLevel(LOG_LEVEL)
    formatter = logging.Formatter(LOG_FORMAT)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)




if __name__ == '__main__':
    set_logging()

    updater = Updater(token=TOKEN)

    main_handler = get_conversation_handler()
    dispatcher = updater.dispatcher
    dispatcher.add_handler(main_handler)

    def loadData():
        try:
            f = open('./backup/conversations.dat', 'rb')
            main_handler.conversations = pickle.load(f)
            f.close()
            f = open('./backup/userdata.dat', 'rb')
            dispatcher.user_data = pickle.load(f)
            f.close()
        except FileNotFoundError:
            logging.error("Data file not found")         
        except:
            logging.error(sys.exc_info()[0])         
 
    def saveData():
        while True:
            time.sleep(SAVE_PERIOD) 
            # Before pickling
            resolved = dict()
            print(type(main_handler.conversations.items()))
            for key, value in main_handler.conversations.items(): 
                print(key, value)
                if isinstance(value, tuple) and len(value) is 2 and isinstance(value[1], promise.Promise):
                    try:
                        new_state = value[1].result()  # Result of async function
                    except: 
                        new_state = value[0]  # In case async function raised an error, fallback to old state
                    resolved[key] = new_state
                else:
                    resolved[key] = value
            try:
                f = open('./backup/conversations.dat', 'wb+')
                pickle.dump(resolved, f)
                f.close()
                f = open('./backup/userdata.dat', 'wb+')
                pickle.dump(dispatcher.user_data, f)
                f.close()
            except:
                logging.error(sys.exc_info()[0])
    
    loadData()
    threading.Thread(target=saveData).start()

    updater.start_polling()
    updater.idle()

