from petri import Place, Transition, PetriNet
import random

CARS_AT_L1_DET_INIT = 0
CARS_AT_L2_DET_INIT = 0
CARS_AT_L3_DET_INIT = 0
CARS_AT_L4_DET_INIT = 0
CARS_AT_L5_DET_INIT = 0
CARS_AT_L6_DET_INIT = 0

CARS_RAND_ADD_RANGE = 1
SIM_ITERATIONS = 10
CARS_IN_PARKING = 5

def intersection_init():

    detection_state_L1 = Place("L1_det", tokens=CARS_AT_L1_DET_INIT)
    detection_state_L2 = Place("L2_det", tokens=CARS_AT_L2_DET_INIT)
    detection_state_L3 = Place("L3_det", tokens=CARS_AT_L3_DET_INIT)
    detection_state_L4 = Place("L4_det", tokens=CARS_AT_L4_DET_INIT)
    detection_state_L5 = Place("L5_det", tokens=CARS_AT_L5_DET_INIT)
    detection_state_L6 = Place("L6_det", tokens=CARS_AT_L6_DET_INIT)

    cars_waiting_L1 = Place("L1_wait")
    cars_waiting_L2 = Place("L2_wait")
    cars_waiting_L3 = Place("L3_wait")
    cars_waiting_L4 = Place("L4_wait")
    cars_waiting_L5 = Place("L5_wait")
    cars_waiting_L6 = Place("L6_wait")

    L1_red_forward = Place("L1_for_R")
    L1_green_forward = Place("L1_for_G")
    L1_red_left = Place("L1_left_R")
    L1_green_left = Place("L1_left_G")

    L2_green_right = Place("L2_right_G")
    L2_red_right = Place("L2_right_R")

    L3_green_right = Place("L3_right_G")
    L3_red_right = Place("L3_right_R")

    L4_red_forward = Place("L4_for_R",)
    L4_green_forward = Place("L4_for_G")
    L4_red_left = Place("L4_left_R",)
    L4_green_left = Place("L4_left_G")

    L5_green_right = Place("L5_right_G")
    L5_red_right = Place("L5_right_R")

    L6_green_right = Place("L6_right_G")
    L6_red_right = Place("L6_right_R")

    R1 = Place("R1", tokens=1)
    R2 = Place("R2", tokens=1)

    cars_in_P1 = Place("P1_cars", tokens = CARS_IN_PARKING)

    cars_gone_by_exit_1 = Place("Exit_1")

    R3 = Place("R3", tokens=1)
    R4 = Place("R4", tokens=1)

    cars_in_P2 = Place("P2_cars", tokens = CARS_IN_PARKING)

    cars_gone_by_exit_2 = Place("Exit_2")

    # Car movement transitions

    L1_cars_arrive = Transition("L1_cars_arrive", inputs = [detection_state_L1], outputs = [cars_waiting_L1])
    L2_cars_arrive = Transition("L2_cars_arrive", inputs = [detection_state_L2], outputs = [cars_waiting_L2])
    L3_cars_arrive = Transition("L3_cars_arrive", inputs = [detection_state_L3], outputs = [cars_waiting_L3])
    L4_cars_arrive = Transition("L4_cars_arrive", inputs = [detection_state_L4], outputs = [cars_waiting_L4])
    L5_cars_arrive = Transition("L5_cars_arrive", inputs = [detection_state_L5], outputs = [cars_waiting_L5])
    L6_cars_arrive = Transition("L6_cars_arrive", inputs = [detection_state_L6], outputs = [cars_waiting_L6])
    
    cars_enter_P1_from_L1 = Transition("cars_enter_P1_from_L1", inputs=[cars_waiting_L1, L1_green_left], outputs=[cars_in_P1])
    cars_enter_P1_from_L2 = Transition("cars_enter_P1_from_L2", inputs=[cars_waiting_L2, L3_green_right], outputs=[cars_in_P1])
    parking_full = Transition("parking_full", inputs=[], full_inputs={cars_in_P1: 5}, outputs=[L1_red_forward, L3_red_right])
    cars_leave_exit_1 = Transition("cars_leave_exit_1", inputs=[cars_in_P1, L2_green_right], outputs=[cars_gone_by_exit_1])
    cars_enter_P2_from_L4 = Transition("cars_enter_P2_from_L4", inputs=[cars_waiting_L4, L4_green_left], outputs=[cars_in_P2])
    cars_enter_P2_from_L5 = Transition("cars_enter_P2_from_L5", inputs=[cars_waiting_L5, L6_green_right], outputs=[cars_in_P2])
    parking_full = Transition("parking_full", inputs=[], full_inputs={cars_in_P2: 5}, outputs=[L4_red_forward, L6_red_right])
    cars_leave_exit_2 = Transition("cars_leave_exit_2", inputs=[cars_in_P2, L6_green_right], outputs=[cars_gone_by_exit_2])

    # Lights operation transitions

    T1 = Transition("T1", inputs=[L1_green_forward, R1], outputs=[L1_red_forward])
    T2 = Transition("T2", inputs=[L1_red_forward], outputs=[L1_green_forward, R1])

    T3 = Transition("T3", inputs=[R1, L1_red_left, R2], ninputs=[cars_in_P1, cars_waiting_L2], outputs=[L1_green_left])
    T4 = Transition("T4", inputs=[L1_green_left], outputs=[R1, L1_red_left, R2])

    T5 = Transition("T5", inputs=[cars_waiting_L3, R2, L3_red_right], ninputs=[cars_waiting_L2, cars_in_P1], outputs=[L3_green_right])
    T6 = Transition("T6", inputs=[L3_green_right], outputs=[R2, L3_red_right])

    T7 = Transition("T7", inputs=[cars_waiting_L2, L2_red_right], outputs=[L2_green_right])
    T8 = Transition("T8", inputs=[L2_green_right], outputs=[L2_red_right])

    T9 = Transition("T1", inputs=[L4_green_forward, R3], outputs=[L4_red_forward])
    T10 = Transition("T2", inputs=[L4_red_forward], outputs=[L4_green_forward, R3])

    T11 = Transition("T3", inputs=[R3, L4_red_left, R4], ninputs=[cars_in_P2, cars_waiting_L5], outputs=[L4_green_left])
    T12 = Transition("T4", inputs=[L4_green_left], outputs=[R3, L4_red_left, R4])

    T13 = Transition("T5", inputs=[cars_waiting_L6, R4, L6_red_right], ninputs=[cars_waiting_L5, cars_in_P2], outputs=[L6_green_right])
    T14 = Transition("T6", inputs=[L6_green_right], outputs=[R4, L6_red_right])

    T15 = Transition("T7", inputs=[cars_waiting_L5, L5_red_right], outputs=[L5_green_right])
    T16 = Transition("T8", inputs=[L5_green_right], outputs=[L5_red_right])

    # Connecting two parking systems
    place_L1_L5 = Place("cars_from_L1_L4")
    place_L3_L4 = Place("cars_from_L3_L5")
    transition_L1_L5 = Transition("transition_L1_L4", inputs=[cars_waiting_L1, L1_green_forward], outputs=[place_L1_L5])
    transition_L3_L4 = Transition("transition_L1_L4", inputs=[cars_waiting_L4, L4_green_forward], outputs=[place_L3_L4])

    transitions = [ L1_cars_arrive, L2_cars_arrive, L3_cars_arrive, 
                    cars_enter_P1_from_L1, cars_enter_P1_from_L2, 
                    parking_full, cars_leave_exit_1, 
                    T1, T2, T3, T4, T5, T6, T7, T8,
                    L4_cars_arrive, L5_cars_arrive, L6_cars_arrive, 
                    cars_enter_P2_from_L4, cars_enter_P2_from_L5, 
                    parking_full, cars_leave_exit_2, 
                    T9, T10, T11, T12, T13, T14, T15, T16,
                    transition_L1_L5, transition_L3_L4]
    
    places = [  detection_state_L1, detection_state_L2, detection_state_L3, 
                cars_waiting_L1, cars_waiting_L2, cars_waiting_L3, 
                L1_red_forward, L1_green_forward, L1_red_left, L1_green_left, 
                L2_green_right, L2_red_right, L3_green_right, L3_red_right, 
                R1, R2, cars_in_P1, cars_gone_by_exit_1,
                detection_state_L4, detection_state_L5, detection_state_L6, 
                cars_waiting_L4, cars_waiting_L5, cars_waiting_L6, 
                L4_red_forward, L4_green_forward, L4_red_left, L4_green_left, 
                L5_green_right, L5_red_right, L6_green_right, L6_red_right, 
                R3, R4, cars_in_P2, cars_gone_by_exit_2,
                place_L1_L5, place_L3_L4]
    
    return transitions, places

def main():

    intersection = PetriNet()
    
    intersection_transitions, intersection_places = intersection_init()

    for place in intersection_places:
        intersection.add_place(place)

    for transition in intersection_transitions:
        intersection.add_transition(transition)        

    intersection.display_places()
    i = 1
    while i <= SIM_ITERATIONS:
        # intersection.add_tokens_to_place("L1_det",random.randint(1,CARS_RAND_ADD_RANGE))
        # intersection.add_tokens_to_place("L6_det",random.randint(1,CARS_RAND_ADD_RANGE))
        
        intersection.fire_transitions_at_random()
        i += 1
    intersection.display_places()

if __name__ == '__main__':
    main()