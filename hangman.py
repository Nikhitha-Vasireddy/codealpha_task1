import random

# Dictionary of 100 words with their categories/hints
word_categories = {
    'python': 'A programming language',
    'hangman': 'A word guessing game',
    'challenge': 'A task that requires effort',
    'programming': 'The act of writing code',
    'random': 'Without a definite aim or pattern',
    'computer': 'An electronic device for processing data',
    'internet': 'A global system of interconnected computer networks',
    'keyboard': 'A peripheral used to input text',
    'algorithm': 'A step-by-step procedure for calculations',
    'database': 'An organized collection of structured information',
    'encryption': 'The process of encoding information',
    'debugging': 'The process of identifying and removing errors',
    'variable': 'A storage location identified by a name in code',
    'function': 'A block of code that performs a specific task',
    'syntax': 'The set of rules that defines the structure of code',
    'compiler': 'A program that translates code into executable form',
    'hardware': 'The physical components of a computer',
    'software': 'The programs and other operating information used by a computer',
    'browser': 'A program used to access the internet',
    'server': 'A computer that provides data to other computers',
    'client': 'A computer that receives data from a server',
    'network': 'A group of interconnected computers',
    'protocol': 'A set of rules governing data communication',
    'firewall': 'A security system for controlling incoming and outgoing network traffic',
    'malware': 'Software designed to disrupt, damage, or gain unauthorized access',
    'virus': 'A malicious program that replicates itself',
    'hacker': 'A person who uses computers to gain unauthorized access',
    'password': 'A string of characters used to gain access to something',
    'authentication': 'The process of verifying the identity of a user',
    'authorization': 'The process of giving someone permission to do something',
    'cryptography': 'The study of secure communication techniques',
    'robotics': 'The branch of technology that deals with the design, construction, and operation of robots',
    'automation': 'The use of technology to perform tasks without human intervention',
    'artificial': 'Made or produced by human beings rather than occurring naturally',
    'intelligence': 'The ability to acquire and apply knowledge and skills',
    'machine': 'A device that uses energy to perform a task',
    'learning': 'The acquisition of knowledge or skills through experience or study',
    'blockchain': 'A decentralized digital ledger that records transactions across many computers',
    'bitcoin': 'A digital currency created in 2009',
    'ethereum': 'A decentralized platform that enables smart contracts',
    'cybersecurity': 'The practice of protecting systems and networks from digital attacks',
    'phishing': 'A type of social engineering attack often used to steal user data',
    'antivirus': 'A software program designed to detect and remove malware',
    'spyware': 'Software that enables a user to obtain covert information about another’s computer activities',
    'trojan': 'A type of malware that misleads users of its true intent',
    'worm': 'A type of malware that spreads copies of itself from computer to computer',
    'exploit': 'A code that takes advantage of a vulnerability in software',
    'zero-day': 'A vulnerability in software that is unknown to the vendor',
    'backdoor': 'A method of bypassing normal authentication to access a system',
    'decryption': 'The process of converting encoded data back to its original form',
    'ransomware': 'A type of malware that threatens to publish or block access to data unless a ransom is paid',
    'intranet': 'A private network accessible only to an organization’s staff',
    'extranet': 'A controlled private network allowing access to partners, vendors, and suppliers',
    'cloud': 'A network of remote servers hosted on the internet to store, manage, and process data',
    'virtualization': 'The creation of a virtual version of something, such as a server or network',
    'hypervisor': 'Software that creates and runs virtual machines',
    'containerization': 'The packaging of software with its dependencies to run consistently across environments',
    'docker': 'A platform that uses OS-level virtualization to deliver software in packages called containers',
    'kubernetes': 'An open-source system for automating deployment, scaling, and management of containerized applications',
    'microservices': 'An architectural style that structures an application as a collection of loosely coupled services',
    'monolith': 'A single, unified application architecture',
    'API': 'A set of functions that allows applications to access data and interact with external software components',
    'REST': 'An architectural style for designing networked applications',
    'SOAP': 'A protocol for exchanging structured information in the implementation of web services',
    'webhook': 'An HTTP callback that sends real-time data to other applications',
    'SDK': 'A collection of software development tools in one installable package',
    'framework': 'A platform for developing software applications',
    'library': 'A collection of pre-written code that can be used in programming',
    'ORM': 'A programming technique for converting data between incompatible systems',
    'CRUD': 'The four basic operations: Create, Read, Update, Delete',
    'SQL': 'A domain-specific language used in programming for managing data in relational databases',
    'NoSQL': 'A class of database management systems that do not use SQL',
    'GraphQL': 'A query language for APIs',
    'CI/CD': 'A method to frequently deliver apps to customers by introducing automation into the stages of app development',
    'DevOps': 'A set of practices that combines software development and IT operations',
    'Agile': 'A set of principles for software development under which requirements and solutions evolve through collaboration',
    'Scrum': 'An agile framework for developing, delivering, and sustaining complex products',
    'Kanban': 'A lean method to manage and improve work across human systems',
    'SaaS': 'A software distribution model in which applications are hosted by a service provider and made available to customers over the internet',
    'PaaS': 'A cloud computing model that delivers tools for developers to create, deploy, and manage applications',
    'IaaS': 'A cloud computing model that provides virtualized computing resources over the internet',
    'Machine Learning': 'A branch of artificial intelligence that focuses on the use of data and algorithms to imitate the way that humans learn',
    'Deep Learning': 'A subset of machine learning in artificial intelligence that has networks capable of learning unsupervised from data that is unstructured or unlabeled',
    'Neural Network': 'A series of algorithms that attempts to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates',
    'Natural Language Processing': 'A branch of artificial intelligence that helps computers understand, interpret and manipulate human language',
    'TensorFlow': 'An open-source library for numerical computation and large-scale machine learning',
    'PyTorch': 'An open-source machine learning library based on the Torch library',
    'Scikit-learn': 'A free software machine learning library for the Python programming language',
    'Keras': 'An open-source software library that provides a Python interface for artificial neural networks'
}

def choose_word():
    word = random.choice(list(word_categories.keys()))
    return word

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def provide_hint(word):
    print(f"Hint: {word_categories[word]}")

def play_game():
    score = 0

    while True:
        word = choose_word()
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6

        print("Let's play Hangman!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                    provide_hint(word)  # Provide a hint based on the word's category
                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

        if guessed:
            print("Congratulations, you guessed the word! Your score increases by 1.")
            score += 1
        else:
            print(f"Sorry, you ran out of tries. The word was {word}. Your score remains {score}.")

        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Your final score is {score}. Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
