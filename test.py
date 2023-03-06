import requests
import clauselocator
from timer import timer
import cProfile
import pstats
from io import StringIO

def run(tests):
    for index, test in enumerate(tests):
        print(f"\ntest {index}: ")
        run_test(test)


@timer
def run_test(test):
    print(f"  text: {test['text']}")
    print(f"  clause: {test['clause']}")
    print(f"  length_text: {len(test['text'])}")
    print(f"  length_clause: {len(test['clause'])}")
    print(f"  expected_result: {test['output']}")
    params = {'text': test["text"], 'sentence': test["clause"]}
    response = requests.get('http://localhost:5000/resource', params=params)
    data = response.json()
    # result = locate_clause(test["text"], test["clause"])
    print(f"  result: {data}")


tests = [
        {
        "text": "This is a legal document. You agree to hold and treat data in the strictest of confidence. If you are in agreement, please sign.",
        "clause": "You agree to hold and treat data in the strictest of confidence.",
        "output": (26, 89)
        },
        {
        "text": "Hello my name is Harry, If you are in agreement",
        "clause": "If you are in agreement then please read",
        "output": (24, 46)
        },
        {
        "text": "If you are in agreement, please return the signed document. You will then be bound to the agreement.",
        "clause": "If you are in agreement, please return the signed document.",
        "output": (0, 58)
        },
        {
        "text": "If you are in agreement, please return the signed document. You will then be bound to the agreement.",
        "clause": "Happy days, If you are in agreement, please return the signed document.",
        "output": (0, 58)
        },
        {
        "text": "the laws of England. You agree that the courts of England have jurisdiction to settle any disputes.",
        "clause": "This Confidentiality Agreement is governed by, and shall be construed in accordance with, the laws of England.",
        "output": (0, 19)
        },
        ]

if __name__ == "__main__":
    # run(tests)
    pr = cProfile.Profile()
    pr.enable()

    run(tests)
    pr.disable()
    # cProfile.run("run(tests)")
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumtime')
    ps.print_stats()

    print(s.getvalue())
