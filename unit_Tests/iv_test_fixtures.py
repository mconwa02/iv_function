import pandas as pd
import numpy as np

feature_one_df = pd.DataFrame(
    np.array(["A", "A", "A", "B", "B", "B", "C", "C", "C", "C", "D", "D"]),
    columns=["f1_all_events_df"],
)

feature_two_df = pd.DataFrame(
    np.array(["X", "X", "Y", "Y", "Y", "Y", "Y", "Y", "Z", "Z"]),
    columns=["f2_all_events_df"],
)

f1_target_df = pd.DataFrame(
    np.array([0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1]), columns=["TARGET"]
)

f2_target_df = pd.DataFrame(
    np.array([1, 0, 1, 0, 0, 0, 0, 0, 1, 0]), columns=["TARGET"]
)

f1_all_events_df = pd.DataFrame(
    np.array([[3, 1, 2], [3, 2, 1], [4, 3, 1], [2, 1, 1]]),
    columns=["COUNT", "EVENT", "NON_EVENT"],
    index=["A", "B", "C", "D"],
    dtype=np.int64,
)

f1_all_events_pct = pd.DataFrame(
    np.array(
        [
            [0.250, 0.143, 0.400],
            [0.250, 0.286, 0.200],
            [0.333, 0.429, 0.200],
            [0.167, 0.143, 0.200],
        ]
    ),
    columns=["COUNT", "EVENT", "NON_EVENT"],
    index=["A", "B", "C", "D"],
    dtype=np.float,
)

f2_all_events_df = pd.DataFrame(
    np.array([[2, 1, 1], [6, 1, 5], [2, 1, 1]]),
    columns=["COUNT", "EVENT", "NON_EVENT"],
    index=["X", "Y", "Z"],
    dtype=np.int64,
)

f2_all_events_pct = pd.DataFrame(
    np.array(
        [
            [0.200, 0.333, 0.143],
            [0.600, 0.333, 0.714],
            [0.200, 0.333, 0.143],
        ]
    ),
    columns=["COUNT", "EVENT", "NON_EVENT"],
    index=["X", "Y", "Z"],
    dtype=np.float,
)

f1_woe = pd.Series(data=[-1.03, 0.36, 0.76, -0.34], index=["A", "B", "C", "D"])
f2_woe = pd.Series(data=[0.85, -0.76, 0.85], index=["X", "Y", "Z"])

f1_iv = 0.49

f2_iv = 0.61
