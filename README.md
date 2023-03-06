Task - "clauselocator"
=================

Core to Robin AI's product is the ability to replace clauses within original client documents, with more suitable replacement clauses.

We require the ability to locate a sentence within text.

The task concerns the design and implementation of an API Endpoint, whose inputs are a sentence and some text. The response from the API should contain the start and end character indexes of the sentence within the text, where they can be found.

1. Design the API Endpoint. This should include the resource name, request and response content, and appropriate response codes.  
2. Implement the API Endpoint using Django/Flask and any libraries you deem appropriate. The endpoint should handle the following cases:
    - Where the whole sentence is contained within the text
    - Where the text starts with some of the end of the sentence
    - Where the text ends with some of the start of the sentence

Don't worry if you do not finish implementing all of the functionailty in 40 minutes - the quality of the code you write is more important than whether the task has been completed. If you do finish, feel free to write some tests to verify the functionality.

Examples:
1. Text: "This is a legal document. You agree to hold and treat data in the strictest of confidence. If you are in agreement, please sign."
Sentence: "You agree to hold and treat data in the strictest of confidence."
In this example, the **start index** is **26**, and the **end index** is **89**.

2. Text: "If you are in agreement, please return the signed document. You will then be bound to the agreement."
Sentence: "If you are in agreement, please return the signed document."
In this example the **start index** is **0**, and the **end index** is **58**.

3. Text: "the laws of England. You agree that the courts of England have jurisdiction to settle any disputes."
Sentence: "This Confidentiality Agreement is governed by, and shall be construed in accordance with, the laws of England."
In this example the **start index** is **0**, and the **end index** is **19**.
