import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def a_press():
    keyboard.press('a')
def b_press():
    keyboard.press('b')
def c_press():
    keyboard.press('c')
def d_press():
    keyboard.press('d')
def e_press():
    keyboard.press('e')
def f_press():
    keyboard.press('f')
def g_press():
    keyboard.press('g')
def h_press():
    keyboard.press('h')
def i_press():
    keyboard.press('i')
def j_press():
    keyboard.press('j')
def k_press():
    keyboard.press('k')
def l_press():
    keyboard.press('l')
def m_press():
    keyboard.press('m')
def n_press():
    keyboard.press('n')
def o_press():
    keyboard.press('o')
def p_press():
    keyboard.press('p')
def q_press():
    keyboard.press('q')
def r_press():
    keyboard.press('r')
def s_press():
    keyboard.press('s')
def t_press():
    keyboard.press('t')
def u_press():
    keyboard.press('u')
def v_press():
    keyboard.press('v')
def w_press():
    keyboard.press('w')
def x_press():
    keyboard.press('x')
def y_press():
    keyboard.press('y')
def z_press():
    keyboard.press('z')


def a_release():
    keyboard.release('a')
def b_release():
    keyboard.release('b')
def c_release():
    keyboard.release('c')
def d_release():
    keyboard.release('d')
def e_release():
    keyboard.release('e')
def f_release():
    keyboard.release('f')
def g_release():
    keyboard.release('g')
def h_release():
    keyboard.release('h')
def i_release():
    keyboard.release('i')
def j_release():
    keyboard.release('j')
def k_release():
    keyboard.release('k')
def l_release():
    keyboard.release('l')
def m_release():
    keyboard.release('m')
def n_release():
    keyboard.release('n')
def o_release():
    keyboard.release('o')
def p_release():
    keyboard.release('p')
def q_release():
    keyboard.release('q')
def r_release():
    keyboard.release('r')
def s_release():
    keyboard.release('s')
def t_release():
    keyboard.release('t')
def u_release():
    keyboard.release('u')
def v_release():
    keyboard.release('v')
def w_release():
    keyboard.release('w')
def x_release():
    keyboard.release('x')
def y_release():
    keyboard.release('y')
def z_release():
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
