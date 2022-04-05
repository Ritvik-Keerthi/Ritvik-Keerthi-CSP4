{% include navigation.html %}

------------------------------------------------
### Create Task Project
------------------------------------------------
## Runtime of Code on Replit with Comments:

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@RitvikKeerthi/Create-Task-FINAL?embed=true"></iframe>

-------------------------------------------------
### Documentation of Create Task Project --> Sports Quiz
-------------------------------------------------
## Final Program Code:

PDF Link to index.html, script. js, style.css: 

---------------------------------------------------
## Independently Create Video

[1 min video that meets CB Create Task requirements](https://drive.google.com/file/d/18ieJcqpVBc8fS6yVZSNVYXWX3YOK0pKS/view?usp=sharing) - Link to under 1 min video under 30 MB fits all requirements

---------------------------------------------------
---------------------------------------------------
## Written Responses

3. WRITTEN RESPONSES (CREATED INDEPENDENTLY)

Submit your responses to prompts 3a – 3d, which are described below. Your
response to all prompts combined must not exceed 750 words (program code
is not included in the word count). Collaboration is not allowed on the written
responses. Instructions for submitting your written responses are available on
the AP Computer Science Principles Exam Page on AP Central.

-----------------------------------------------------------------------
3a. Provide a written response that does all three of the following:
Approx. 150 words (for all subparts of 3a combined)

i. Describes the overall purpose of the program
- The purpose of this program is to act as a sports quiz. It is to give the user more information on different sports, such as but not limited to tennis, golf, basketball, football, and baseball. 

ii. Describes what functionality of the program is demonstrated in
the video
- The functionality of the program demonstrated in the video would be the ability to have correct answers highlighted in green (on user click) and incorrect answers highlighted in red (on user click). 

iii. Describes the input and output of the program demonstrated in
the video
- The input would be when the user clicks on a specific answer choice, with there being 4 options. The output would be the score, grade, and message that the user receives after the completion of the quiz. 

----------------------------------------------------------------------
3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program. Approx. 200 words (for all subparts of 3b combined, exclusive of
program code)

i. The first program code segment must show how data have been
stored in the list. 
- Data is being stored in the list, in the form of questions for the user. In this case, it is formed using a constant, titled Questions. 
```
const questions = [
            {
                question: "How many NBA championships have the Lakers won?",
                A: "17 chips",
                B: "7 chips",
                C: "25 chips",
                D: "33 chips",
                Answer: "A"
            },

            {
                question: "How many seasons has Tom Brady played in the NFL?",
                A: "10 seasons",
                B: "20 seasons",
                C: "17 seasons",
                D: "19 seasons",
                Answer: "B"
            },

            {
                question: "Who has the fastest serve in Tennis?",
                A: "Nathan Shih",
                B: "Rafael Nadal",
                C: "Roger Federer",
                D: "Sam Groth",
                Answer: "D"
            },

            {
                question: "Who is the best Golf player below?",
                A: "Tyreek Hill",
                B: "Tiger Woods",
                C: "Jeremy Lin",
                D: "Fernando Tatis Jr",
                Answer: "B"
            },

            {
                question: "How long is an NBA game, without overtimes?",
                A: "49 minutes",
                B: "47 minutes",
                C: "50 minutes",
                D: "48 minutes",
                Answer: "D"
            },

            {
                question: "How many people watched the Super Bowl last year {2021}?",
                A: "67 million",
                B: "252 million",
                C: "96 million",
                D: "87 million",
                Answer: "C"
            },

            {
                question: "Which team finished at the top of the NFC in the 2021-2022 season?",
                A: "Arizona Cardinals",
                B: "Dallas Cowboys",
                C: "Green Bay Packers",
                D: "Brooklyn Nets",
                Answer: "C"
            },

            {
                question: "How many points is a field goal worth in American football?",
                A: "3",
                B: "4",
                C: "1",
                D: "67",
                Answer: "A"
            },

            {
                question: "In American football, how many minutes is a quarter?",
                A: "16",
                B: "23",
                C: "7",
                D: "15",
                Answer: "D"
            },

            {
                question: "How many basketball teams are there in the NBA?",
                A: "23",
                B: "32",
                C: "31",
                D: "30",
                Answer: "D"
            },

            {
                question: "Where are the Knicks located?",
                A: "New York",
                B: "California",
                C: "New Jersey",
                D: "Los Angeles",
                Answer: "A"
            },


            {
                question: "Who was the NBA MVP in 2020?",
                A: "Giannis Antetokounmpo",
                B: "LeBron James",
                C: "Kevin Durant",
                D: "Kyrie Irving",
                Answer: "A"
            },

            {
                question: "Which of the following is a tennis player?",
                A: "Roger Federer",
                B: "LeBron James",
                C: "Leonard Fournette",
                D: "Tom Brady",
                Answer: "A"
            }

        ]

```

ii. The second program code segment must show the data in the
same list being used, such as creating new data from the existing
data or accessing multiple elements in the list, as part of fulfilling
the program’s purpose. 
- In this code segment, the questions are being shuffled in random order, as there are > 10 questions in the constant. Only 10 questions are used (randomnly) for this program at once. 
```
let shuffledQ = []

        function handleQuestions() {
            while (shuffledQ.length <= 9) {
                const random = questions[Math.floor(Math.random() * questions.length)]
                if (!shuffledQ.includes(random)) {
                    shuffledQ.push(random)
                }
            }
        }
```

iii. Identifies the name of the list being used in this response.
- The list name being used in this response is titled "questions"

iv. Describes what the data contained in the list represent in your program.
- The data contained in the list represents the question bank that can be prompted to the user in order for them to answer. 

v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list. 
- This program would not be able to be written without this list, as a quiz always requires a question and an answer. The only other way to do this would be to manually write out every question with every possible answer, which proves to be extremely inefficient. Overall, this list is necessary for the program to be functioning, making it an integral part of the code. 

-----------------------------------------------------------------------
3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. 
Approx. 200 words (for all subparts of 3c combined, exclusive of program code)

i. The first program code segment must be a student-developed
procedure that:

□ Defines the procedure’s name and return type (if necessary)

□ Contains and uses one or more parameters that have an effect
on the functionality of the procedure

□ Implements an algorithm that includes sequencing, selection,
and iteration 
```
function NextQuestion(index) {
            handleQuestions()
            const currentQuestion = shuffledQ[index]
            document.getElementById("QNum").innerHTML = questionNumber
            document.getElementById("current-score").innerHTML = score
            document.getElementById("display-question").innerHTML = currentQuestion.question;
            document.getElementById("option-1").innerHTML = currentQuestion.A;
            document.getElementById("option-2").innerHTML = currentQuestion.B;
            document.getElementById("option-3").innerHTML = currentQuestion.C;
            document.getElementById("option-4").innerHTML = currentQuestion.D;

        }
function checkForAnswer() {
            const currentQuestion = shuffledQ[indexNumber]
            const currentQuestionAnswer = currentQuestion.Answer
            const options = document.getElementsByName("option");
            let Answer = null

            options.forEach((option) => {
                if (option.value === currentQuestionAnswer) {
                    Answer = option.labels[0].id
                }
            })

            if (options[0].checked === false && options[1].checked === false && options[2].checked === false && options[3].checked == false) {
                document.getElementById('option-modal').style.display = "flex"
            }

            options.forEach((option) => {
                if (option.checked === true && option.value === currentQuestionAnswer) {
                    document.getElementById(Answer).style.backgroundColor = "green"
                    score++
                    indexNumber++
                    setTimeout(() => {
                        questionNumber++
                    }, 1000)
                }

                else if (option.checked && option.value !== currentQuestionAnswer) {
                    const wrongLabelId = option.labels[0].id
                    document.getElementById(wrongLabelId).style.backgroundColor = "red"
                    document.getElementById(Answer).style.backgroundColor = "green"
                    wrongAttempt++
                    indexNumber++
                    setTimeout(() => {
                        questionNumber++
                    }, 1000)
                }
            })
        }
```

ii. The second program code segment must show where your
student-developed procedure is being called in your program.
```
function NextQ() {
            checkForAnswer()
            unCheckRadioButtons()
            setTimeout(() => {
                if (indexNumber <= 9) {
                    NextQuestion(indexNumber)
                }
                else {
                    EndGame()
                }
                resetBackground()
            }, 1000);
        }
```

iii. Describes in general what the identified procedure does and how it
contributes to the overall functionality of the program
- There are two separate procedures in this code segment, however, both of them are utilized together. In the first procedure, the function moves to the next Question given the answer choice, using document.getElementById, taking the paramater of index. In the second procedure, iteration, sequencing, and selection are used with the foreach loops, if statements, and code sequence. This procedure in particular checks if the user has inputted a correct answer and redirects them to the proper prompt. 

iv. Explains in detailed steps how the algorithm implemented in the
identified procedure works. Your explanation must be detailed
enough for someone else to recreate it.
- In this particular algorithm of checking the answer, variables are created to store the currentquestion and the answer to that currentquestion, as well as a variable for the answer options. To begin, the answer starts off at null, but changes depending on the variable option, or what the user inputs. For the correct option, the score value goes up by 1, the index value goes up by 1, and the question number goes up by 1. Otherwise, if a wrong option is inputted, the score does not increase, the index number goes up by 1, and the wrong attempt constant goes up by 1, as well as the question number. This function is now called in the NextQ function in which the user is directed to the next question, and the process starts all over again. 

-----------------------------------------------------------------------
3d. Provide a written response that does all three of the following:
Approx 200 words (for all subparts of 3d combined)

i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.

First call: In the checkAnswer procedure, if the option variable gets an argument with the correct answer, it will increase the score and go onto the next question. 
```
options.forEach((option) => {
                if (option.value === currentQuestionAnswer) {
                    Answer = option.labels[0].id
                }
            })

            if (options[0].checked === false && options[1].checked === false && options[2].checked === false && options[3].checked == false) {
                document.getElementById('option-modal').style.display = "flex"
            }
```

Second call: In the checkAnswer procedure, if the option variable gets an argument with the wrong answer, it will not change the score, but goes onto the next question. 
```
options.forEach((option) => {
                if (option.checked === true && option.value === currentQuestionAnswer) {
                    document.getElementById(Answer).style.backgroundColor = "green"
                    score++
                    indexNumber++
                    setTimeout(() => {
                        questionNumber++
                    }, 1000)
                }

                else if (option.checked && option.value !== currentQuestionAnswer) {
                    const wrongLabelId = option.labels[0].id
                    document.getElementById(wrongLabelId).style.backgroundColor = "red"
                    document.getElementById(Answer).style.backgroundColor = "green"
                    wrongAttempt++ //adds 1 to wrong attempts
                    indexNumber++
                    //set to delay question number till when next question loads
                    setTimeout(() => {
                        questionNumber++
                    }, 1000)
                }
            })
        }
```
ii. Describes what condition(s) is being tested by each call to the
procedure

Condition(s) tested by the first call: Answer is correct by user input (true condition)

Condition(s) tested by the second call: If answer is not correct by user input (false condition)


iii. Identifies the result of each call

Result of the first call: Score variable increases, index number increases, moves onto next question

Result of the second call: Score variable stays the same, index number increases, question number increases, wrong attempt variable increases

---------------------------------------------------------------
END OF WRITTEN RESPONSES
