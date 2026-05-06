import numpy as np

def frequency_response(system, freq):
    omega = 2 * np.pi * freq
    responses = []

    for w in omega:
        A = -w**2 * system.M + 1j*w*system.C + system.K
        F = np.array([1, 0])

        X = np.linalg.solve(A, F)
        responses.append(X)

    return np.array(responses)
