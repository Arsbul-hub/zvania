from kivy.uix.screenmanager import NoTransition


def switch_to(container, current, transition=NoTransition):
    container.transition = transition
    container.current = current
    container.get_screen(current).on_switch_bind()