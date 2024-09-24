import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def a_press():
    keyboard.press('a')
    keyboard.release('a')
def b_press():
    keyboard.press('b')
    keyboard.release('b')
def c_press():
    keyboard.press('c')
    keyboard.release('d')
def d_press():
    keyboard.press('d')
    keyboard.release('d')
def e_press():
    keyboard.press('e')
    keyboard.release('e')
def f_press():
    keyboard.press('f')
    keyboard.release('f')
def g_press():
    keyboard.press('g')
    keyboard.release('g')
def h_press():
    keyboard.press('h')
    keyboard.release('h')
def i_press():
    keyboard.press('i')
    keyboard.release('i')
def j_press():
    keyboard.press('j')
    keyboard.release('j')
def k_press():
    keyboard.press('k')
    keyboard.release('k')
def l_press():
    keyboard.press('l')
    keyboard.release('l')
def m_press():
    keyboard.press('m')
    keyboard.release('m')
def n_press():
    keyboard.press('n')
    keyboard.release('n')
def o_press():
    keyboard.press('o')
    keyboard.release('o')
def p_press():
    keyboard.press('p')
    keyboard.release('p')
def q_press():
    keyboard.press('q')
    keyboard.release('q')
def r_press():
    keyboard.press('r')
    keyboard.release('r')
def s_press():
    keyboard.press('s')
    keyboard.release('s')
def t_press():
    keyboard.press('t')
    keyboard.release('t')
def u_press():
    keyboard.press('u')
    keyboard.release('u')
def v_press():
    keyboard.press('v')
    keyboard.release('v')
def w_press():
    keyboard.press('w')
    keyboard.release('w')
def x_press():
    keyboard.press('x')
    keyboard.release('x')
def y_press():
    keyboard.press('y')
    keyboard.release('y')
def z_press():
    keyboard.press('z')
    keyboard.release('z')



def space_press():
    keyboard.press(' ')
def enter_press():
    keyboard.press("""
""")
def delete_press():
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
def playpause_press():
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)
def previous_press():
    keyboard.press(Key.media_previous)
    keyboard.release(Key.media_previous)
def next_press():
    keyboard.press(Key.media_next) 
    keyboard.release(Key.media_next)
def volume_up_press():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)
def volume_down_press():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)


def space_release():
    keyboard.release(' ')
def enter_release():
    keyboard.release("""
""")
