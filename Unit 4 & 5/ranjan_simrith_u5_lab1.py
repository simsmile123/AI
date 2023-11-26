from pomegranate import *
Graduate = DiscreteDistribution({'g':0.9, 'not-g':0.1})
Tester1 = ConditionalProbabilityTable([ #you need a tester for each outcome
['g', 'pos', 0.5],
['g', 'not-pos', 0.5],
['not-g', 'pos', 0.05],
['not-g', 'not-pos]', 0.95]], [Graduate])
Tester2 = ConditionalProbabilityTable([
['g', 'pos', 0.75],
['g', 'not-pos', 0.25],
['not-g', 'pos', 0.25],
['not-g', 'not-pos', 0.75]], [Graduate])
s_grad = State(Graduate, 'graduate')
s_tester_1 = State(Tester1, 'tester_1')
s_tester_2 = State(Tester2, 'tester_2')
model = BayesianNetwork('graduate')
model.add_states(s_grad, s_tester_1, s_tester_2)
model.add_transition(s_grad, s_tester_1)
model.add_transition(s_grad, s_tester_2)
model.bake() # finalize the topology of the model
print ('The number of nodes:', model.node_count())
print ('The number of elges:', model.edge_count())
# predict_proba(Given factors)
# tester 1 has all of 01 cases, tester 2 has all of 02 cases, pos/not-pos refers to if they got 01/02 or if they didnt
print(model.predict_proba({'tester_1':'not-pos', 'graduate' :'g'})[2].parameters) #a
print(model.predict_proba({'tester_1': 'pos', 'tester_2': 'pos'})[0].parameters) #b
#[0] translates to given graduade, [1] translates to given 01, [2] is 02
print(model.predict_proba({'tester_1': 'not-pos', 'tester_2': 'pos'})[0].parameters) #c
print(model.predict_proba({'tester_1': 'not-pos', 'tester_2': 'not-pos'})[0].parameters) #d
print(model.predict_proba({'tester_2': 'pos'})[1].parameters) #e


