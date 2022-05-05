# Q6. Write a program to implement the Viterbi Algorithm. 
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

	 
def dptable(V):
     
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

def viterbi_algorithm(observations, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][observations[0]], "prev": None}

    for t in range(1, len(observations)):
        V.append({})
        for st in states:
            max_tr_prob = V[t - 1][states[0]]["prob"] * trans_p[states[0]][st]
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                tr_prob = V[t - 1][prev_st]["prob"] * trans_p[prev_st][st]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    prev_st_selected = prev_st

            max_prob = max_tr_prob * emit_p[st][observations[t]]
            V[t][st] = {"prob": max_prob, "prev": prev_st_selected}

    for line in dptable(V):
        print(line)
 
    opt = []
    max_prob = 0.0
    best_st = None
 
    for st, data in V[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st
 
 
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
 
    print ("The steps of states are " + " ".join(opt) + " with highest probability of %s" % max_prob)
if __name__ == '__main__':
    observations = ("normal", "cold", "dizzy")
    states = ("Healthy", "Fever")
    start_p = {"Healthy": 0.6, "Fever": 0.4}
    trans_p = {
        "Healthy": {"Healthy": 0.8, "Fever": 0.2},
        "Fever": {"Healthy": 0.3, "Fever": 0.7},
    }
    emit_p = {
        "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
        "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
    }

    viterbi_algorithm(observations=observations, states= states, start_p=start_p, trans_p=trans_p, emit_p=emit_p)