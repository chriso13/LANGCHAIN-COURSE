from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 


load_dotenv() 
def main() -> None:
    print("Hello from langchain-course!")
    information ="""
        William Henry Gates III (born October 28, 1955) is an American businessman and philanthropist. A pioneer of the microcomputer revolution of the 1970s and 1980s, he co-founded the software company Microsoft in 1975 with his childhood friend Paul Allen. Following Microsoft's initial public offering in 1986 and the subsequent increase in its stock price, Gates became the world's then-youngest billionaire in 1987, at age 31. Forbes magazine ranked him as the world's wealthiest person in their The World's Billionaires list for 18 out of 24 years between 1995 and 2017, including 13 years consecutively from 1995 to 2007. Gates became the first centibillionaire in 1999, when his net worth briefly surpassed US$100 billion. According to Forbes, as of July 2026, his net worth stood at US$106.5 billion, making him the 19th-wealthiest individual in the world.

Born and raised in Seattle, Washington, Gates was privately educated at Lakeside School, where he befriended Allen and developed his computing interests. In 1973, he enrolled at Harvard University, where he took classes including Math 55 and graduate-level computer science courses, but he dropped out in 1975 to co-found and lead Microsoft. He served as its CEO for the next 25 years and also became president and chairman of the board when the company was incorporated in 1981. Succeeded as CEO by Steve Ballmer in 2000, he transitioned to chief software architect, a position he held until 2008. He stepped down as chairman of the board in 2014 and became technology adviser to CEO Satya Nadella and other Microsoft leaders, a position he still holds. He resigned from the board in 2020.

Over time, Gates reduced his role at Microsoft to focus on his philanthropic work with the Bill & Melinda Gates Foundation, the world's largest private charitable organization, which he and his then-wife, Melinda French Gates, co-chaired from 2000 until 2024. Focusing on areas including health, education, and poverty alleviation, Gates became known for his efforts to combat transmissible diseases such as tuberculosis, malaria, and polio. After French Gates resigned as co-chair following the couple's divorce, the foundation was renamed the Gates Foundation, with Gates as its sole chair.

Gates is the founder and chairman of several other companies, including BEN, Cascade Investment, TerraPower, Gates Ventures, and Breakthrough Energy. In 2010, he and Warren Buffett founded the Giving Pledge, whereby they and other billionaires pledged to give at least half their wealth to philanthropy. Named as one of the 100 most influential people of the 20th century by Time magazine in 1999, he has received numerous other honors and accolades, including a Presidential Medal of Freedom, awarded jointly to him and French Gates in 2016 for their philanthropic work. The subject of several documentary films, he published the first of three planned memoirs, Source Code: My Beginnings, in 2025.

Early life and education
William Henry Gates III was born on October 28, 1955, in Seattle, Washington,[1] as the only son of Bill Gates Sr.[a] (1925–2020) and his first wife, Mary Maxwell Gates (1929–1994).[2] His ancestry includes English, German, and Irish/Scots-Irish.[3] His father was a prominent lawyer, and his mother served on the board of directors of First Interstate BancSystem and United Way of America. Gates's maternal grandfather, J. W. Maxwell, was a national bank president. Gates also has an older sister, Kristi (Kristianne), and a younger sister, Libby. He is the fourth of his name in his family, but is known as William Gates III or "Trey" (i.e., three) because his father had the "II" suffix.[4][5] The family lived in the Sand Point area of Seattle in a home that was damaged by a rare tornado when Gates was 7.[6]

When Gates was young, his parents wanted him to pursue a career in law.[7] During his childhood, his family regularly attended a church of the Congregational Christian Churches, a Protestant Reformed denomination.[8][9][10]

Gates was small for his age and was bullied as a child.[5] The family encouraged competition; one visitor reported that "it didn't matter whether it was hearts or pickleball or swimming to the dock; there was always a reward for winning, and there was always a penalty for losing".[11]


Gates (right) with Paul Allen seated at Teletype Model 33 ASR terminals in Lakeside School, 1970
At age 13, Gates enrolled in the private Lakeside Prep School.[12][13] When he was in the eighth grade, the Mothers' Club at the school used proceeds from Lakeside School's rummage sale to buy a Teletype Model 33 ASR terminal and a block of computer time on a General Electric (GE) computer for the students.[14] Gates took an interest in programming the GE system in BASIC, and he was excused from math classes to pursue his interest. He wrote his first computer program on this machine, an implementation of tic-tac-toe that allowed users to play games against the computer. Gates was fascinated by the machine and how it would always execute software code perfectly.[15]

After the Mothers Club donation was exhausted, Gates and other students sought time on systems, including DEC PDP minicomputers. One of these systems was a PDP-10 belonging to Computer Center Corporation (CCC), which banned Gates, Paul Allen, Ric Weiland, and Gates's best friend and first business partner, Kent Evans, for the summer after it caught them exploiting bugs in the operating system to obtain free computer time.[16][5]

The four students formed the Lakeside Programmers Club to make money.[5] At the end of the ban, they offered to find bugs in CCC's software in exchange for extra computer time. Rather than using the system remotely via Teletype, Gates went to CCC's offices and studied source code for various programs that ran on the system, including Fortran, Lisp, and machine language. The arrangement with CCC continued until 1970, when the company went out of business.[5]

In 1971, a Lakeside teacher enlisted Gates and Evans to automate the school's class-scheduling system, providing them computer time and royalties in return. The duo worked diligently in order to have the program ready for their senior year. Towards the end of their junior year, Evans was killed in a mountain climbing accident, which Gates described as one of the saddest days of his life. He then turned to Allen, who helped him finish the system for Lakeside.[5]

At age 17, Gates formed a venture with Allen called Traf-O-Data to make traffic counters based on the Intel 8008 processor.[17] In 1972, he served as a congressional page in the House of Representatives.[18][19] He was a national merit scholar when he graduated from Lakeside School in 1973.[20] He scored 1590 out of 1600 on the SAT and enrolled at Harvard University in the autumn of 1973.[21][22]

Gates did not stay at Harvard long enough to choose a concentration, but took mathematics (including Math 55) and graduate-level computer science courses.[23] While at Harvard, he met fellow student and future Microsoft CEO Steve Ballmer. Gates left Harvard after two years while Ballmer stayed and graduated magna cum laude. Years later, Ballmer succeeded Gates as Microsoft's CEO and maintained that position from 2000 until his resignation in 2014.[24][25]

Gates devised an algorithm for pancake sorting as a solution to one of a series of unsolved problems[26] presented in a combinatorics class by Professor Harry Lewis. His solution held the record as the fastest version for over 30 years, and its successor is faster by only 2%.[27] His solution was formalized and published in collaboration with Harvard computer scientist Christos Papadimitriou.[28]

Gates remained in contact with Paul Allen and joined him at Honeywell during the summer of 1974.[29] In 1975, the MITS Altair 8800 was released based on the Intel 8080 CPU, and Gates and Allen saw the opportunity to start their own computer software company.[30] Gates dropped out of Harvard that same year. His parents were supportive of him after seeing how much he wanted to start his own company.[31] He explained his decision to leave Harvard

    """

    summary_prompt= """
    given the information {information} about a person I want you create:
    1. A short summary
    2. two interesting fact about them 

    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_prompt
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(response.content)
 
if __name__ == "__main__":
    main()
