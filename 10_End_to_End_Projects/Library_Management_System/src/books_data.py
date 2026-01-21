# ____________________Describe the Dictionary implement logic______________________

# book ID ------> Title ------>Author


CS_BOOKS = [
    {"id": "CS101", "title": "Introduction to Algorithms", "author": "Cormen"},
    {"id": "CS102", "title": "Operating System Concepts", "author": "Silberschatz"},
    {"id": "CS103", "title": "Computer Networks", "author": "Tanenbaum"},
    {"id": "CS104", "title": "Database System Concepts", "author": "Korth"},
    {"id": "CS105", "title": "Modern Operating Systems", "author": "Tanenbaum"},
    {"id": "CS106", "title": "Compilers: Principles, Techniques", "author": "Aho"},
    {"id": "CS107", "title": "Computer Organization", "author": "Patterson"},
    {"id": "CS108", "title": "Distributed Systems", "author": "Tanenbaum"},
    {"id": "CS109", "title": "Software Engineering", "author": "Pressman"},
    {"id": "CS110", "title": "Clean Architecture", "author": "Robert C. Martin"}
]

AI_BOOKS = [
    {"id": "AI201", "title": "AI: A Modern Approach", "author": "Russell"},
    {"id": "AI202", "title": "Pattern Recognition and ML", "author": "Bishop"},
    {"id": "AI203", "title": "Hands-On Machine Learning", "author": "Géron"},
    {"id": "AI204", "title": "Deep Learning", "author": "Goodfellow"},
    {"id": "AI205", "title": "Machine Learning", "author": "Tom Mitchell"},
    {"id": "AI206", "title": "Neural Networks", "author": "Haykin"},
    {"id": "AI207", "title": "Reinforcement Learning", "author": "Sutton"},
    {"id": "AI208", "title": "Computer Vision", "author": "Szeliski"},
    {"id": "AI209", "title": "Speech and Language Processing", "author": "Jurafsky"},
    {"id": "AI210", "title": "Probabilistic Graphical Models", "author": "Koller"}
]

PL_BOOKS = [
    {"id": "PL301", "title": "The C Programming Language", "author": "Kernighan"},
    {"id": "PL302", "title": "Effective Java", "author": "Joshua Bloch"},
    {"id": "PL303", "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": "PL304", "title": "Fluent Python", "author": "Luciano Ramalho"},
    {"id": "PL305", "title": "Programming in C++", "author": "Bjarne Stroustrup"},
    {"id": "PL306", "title": "Go Programming Language", "author": "Alan Donovan"},
    {"id": "PL307", "title": "Rust Programming Language", "author": "Steve Klabnik"},
    {"id": "PL308", "title": "JavaScript: The Good Parts", "author": "Douglas Crockford"},
    {"id": "PL309", "title": "Scala for the Impatient", "author": "Cay Horstmann"},
    {"id": "PL310", "title": "Kotlin in Action", "author": "Dmitry Jemerov"}
]

MATH_BOOKS = [
    {"id": "MA401", "title": "Linear Algebra", "author": "Gilbert Strang"},
    {"id": "MA402", "title": "Calculus", "author": "Stewart"},
    {"id": "MA403", "title": "Discrete Mathematics", "author": "Rosen"},
    {"id": "MA404", "title": "Probability Theory", "author": "Sheldon Ross"},
    {"id": "MA405", "title": "Numerical Methods", "author": "Burden"},
    {"id": "MA406", "title": "Engineering Mathematics", "author": "Kreyszig"},
    {"id": "MA407", "title": "Vector Calculus", "author": "Marsden"},
    {"id": "MA408", "title": "Complex Analysis", "author": "Churchill"},
    {"id": "MA409", "title": "Statistics", "author": "Walpole"},
    {"id": "MA410", "title": "Graph Theory", "author": "Bondy"}
]

DS_BOOKS = [
    {"id": "DS501", "title": "Data Science from Scratch", "author": "Joel Grus"},
    {"id": "DS502", "title": "Python for Data Analysis", "author": "Wes McKinney"},
    {"id": "DS503", "title": "Hands-On Data Science", "author": "Jake VanderPlas"},
    {"id": "DS504", "title": "Big Data Analytics", "author": "Seema Acharya"},
    {"id": "DS505", "title": "Data Mining Concepts", "author": "Han"},
    {"id": "DS506", "title": "Practical Statistics", "author": "Bruce"},
    {"id": "DS507", "title": "Spark: The Definitive Guide", "author": "Bill Chambers"},
    {"id": "DS508", "title": "Storytelling with Data", "author": "Cole Knaflic"},
    {"id": "DS509", "title": "Feature Engineering", "author": "Kuhn"},
    {"id": "DS510", "title": "SQL for Data Science", "author": "Renee Teate"}
]

SYS_BOOKS = [
    {"id": "SY601", "title": "Operating Systems", "author": "Galvin"},
    {"id": "SY602", "title": "Computer Architecture", "author": "Hennessy"},
    {"id": "SY603", "title": "Linux Kernel Development", "author": "Robert Love"},
    {"id": "SY604", "title": "Advanced Programming in UNIX", "author": "Stevens"},
    {"id": "SY605", "title": "System Programming", "author": "Dhamdhere"},
    {"id": "SY606", "title": "Embedded Systems", "author": "Raj Kamal"},
    {"id": "SY607", "title": "Operating System Design", "author": "Tanenbaum"},
    {"id": "SY608", "title": "Compilers", "author": "Aho"},
    {"id": "SY609", "title": "Linkers and Loaders", "author": "Levine"},
    {"id": "SY610", "title": "Virtual Machines", "author": "Smith"}
]

SEC_BOOKS = [
    {"id": "CY701", "title": "Cryptography and Network Security", "author": "Stallings"},
    {"id": "CY702", "title": "Web Application Security", "author": "Stuttard"},
    {"id": "CY703", "title": "Hacking: The Art of Exploitation", "author": "Erickson"},
    {"id": "CY704", "title": "Metasploit", "author": "Kennedy"},
    {"id": "CY705", "title": "Network Security Essentials", "author": "Stallings"},
    {"id": "CY706", "title": "Practical Malware Analysis", "author": "Sikorski"},
    {"id": "CY707", "title": "The Web Hacker's Handbook", "author": "Stuttard"},
    {"id": "CY708", "title": "Cybersecurity Essentials", "author": "Cisco"},
    {"id": "CY709", "title": "Penetration Testing", "author": "Georgia Weidman"},
    {"id": "CY710", "title": "Security Engineering", "author": "Ross Anderson"}
]

ELEC_BOOKS = [
    {"id": "EL801", "title": "Digital Electronics", "author": "Morris Mano"},
    {"id": "EL802", "title": "Microprocessors", "author": "Gaonkar"},
    {"id": "EL803", "title": "Embedded Systems", "author": "Raj Kamal"},
    {"id": "EL804", "title": "Analog Electronics", "author": "Sedra"},
    {"id": "EL805", "title": "VLSI Design", "author": "Weste"},
    {"id": "EL806", "title": "Electrical Machines", "author": "Bimbhra"},
    {"id": "EL807", "title": "Control Systems", "author": "Ogata"},
    {"id": "EL808", "title": "Signals and Systems", "author": "Oppenheim"},
    {"id": "EL809", "title": "Power Electronics", "author": "Rashid"},
    {"id": "EL810", "title": "Robotics", "author": "Craig"}
]

CP_BOOKS = [
    {"id": "CP901", "title": "Competitive Programming", "author": "Halim"},
    {"id": "CP902", "title": "Programming Challenges", "author": "Skiena"},
    {"id": "CP903", "title": "Guide to Competitive Programming", "author": "Laaksonen"},
    {"id": "CP904", "title": "Algorithm Design Manual", "author": "Skiena"},
    {"id": "CP905", "title": "Cracking the Coding Interview", "author": "Gayle Laakmann"},
    {"id": "CP906", "title": "Elements of Programming Interviews", "author": "Adnan Aziz"},
    {"id": "CP907", "title": "DSA Made Easy", "author": "Narasimha"},
    {"id": "CP908", "title": "Problem Solving Strategies", "author": "Brassard"},
    {"id": "CP909", "title": "Algorithms Unlocked", "author": "Cormen"},
    {"id": "CP910", "title": "Coding Interview Handbook", "author": "Alex Xu"}
]

GEN_BOOKS = [
    {"id": "GN1001", "title": "Encyclopedia of Science", "author": "Britannica"},
    {"id": "GN1002", "title": "Engineering Handbook", "author": "McGraw Hill"},
    {"id": "GN1003", "title": "Research Methodology", "author": "Kothari"},
    {"id": "GN1004", "title": "Technical Writing", "author": "Mike Markel"},
    {"id": "GN1005", "title": "Innovation and Entrepreneurship", "author": "Peter Drucker"},
    {"id": "GN1006", "title": "Career Guidance", "author": "Dale Carnegie"},
    {"id": "GN1007", "title": "Soft Skills", "author": "Alex"},
    {"id": "GN1008", "title": "Time Management", "author": "Brian Tracy"},
    {"id": "GN1009", "title": "Leadership", "author": "John Maxwell"},
    {"id": "GN1010", "title": "General Knowledge", "author": "Arihant"}
]

# __________ when someone enter any key then i will call this according the key user entered ________________
BOOKS_BY_CATEGORY = {  # 1,2,.....10 all are the category_key
    "1": {"name": "Computer Science", "books": CS_BOOKS},
    "2": {"name": "AI & Machine Learning", "books": AI_BOOKS},
    "3": {"name": "Programming Languages", "books": PL_BOOKS},
    "4": {"name": "Mathematics", "books": MATH_BOOKS},
    "5": {"name": "Data Science & Big Data", "books": DS_BOOKS},
    "6": {"name": "Systems & Low-Level Engineering", "books": SYS_BOOKS},
    "7": {"name": "Cyber Security", "books": SEC_BOOKS},
    "8": {"name": "Electronics & Hardware", "books": ELEC_BOOKS},
    "9": {"name": "Competitive Programming", "books": CP_BOOKS},
    "10": {"name": "General & Reference", "books": GEN_BOOKS},
}

# for category_key, category_data in BOOKS_BY_CATEGORY.items():
#     print(f"{category_key}. {category_data['name']}")

# this is just check that all are run correctly or not
