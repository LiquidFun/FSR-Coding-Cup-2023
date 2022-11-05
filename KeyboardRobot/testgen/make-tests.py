from pathlib import Path
import subprocess
import string
import random

import numpy as np


seed = 1985168
np.random.seed(seed)
random.seed(seed)
randint = random.randint

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "prioqueue.py"

def write_test(name, kb: str, words: str):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        for i in range(0, 36, 6):
            file.write(f"{kb[i:i+6]}\n")
        file.write(f"{words}\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)

def make_random():
    letters = list(string.ascii_lowercase + "_" + ("." * (36 - 27)))
    random.shuffle(letters)
    letters = ''.join(letters)
    n = randint(1, 200)
    words = ''.join(np.random.choice(list(string.ascii_lowercase + '_'), size=n, replace=True))
    return letters, words


def main():
    index = 1

    sample_test_cases = [
        (".rsft..qedu..pacih.zbmjg.yolkn._xwv.", "hello_my_great_friend_i_have_not_seen_you_in_a_long_time"),
        (".rsft..qedu..pacih.zbmjg.yolkn._xwv.", "this_problem_is_veeeery_easy"),
        ("abcdef.....gstuv.hr_.w.iqzyx.jponmlk", "a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z"),
        ("abcdef.....gstuv.hr_.w.iqzyx.jponmlk", "abcdefghijklmnopqrstuvwxyz"),
        ("abcdef..._.gstuv.hr..w.iqzyx.jponmlk", "____x____y____z"),
        ("abcdef..._.gstuv.hr..w.iqzyx.jponmlk", "akakakakakakakakakak"),
        ("abcdef..._.gstuv.hr..w.iqzyx.jponmlk", "ffffffffffffffffffffff"),
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", *inputs)
        index += 1

    tests_to_be_created = {
        make_random: 100,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__[5:]
            write_test(f"{index:03}-{name}", *func())
            index += 1



if __name__ == "__main__":
    main()
