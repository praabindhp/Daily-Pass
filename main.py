import os

def makeCommits (days):
    if days < 0:
        os.system('git push')
    
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:

            file.write(f'{dates} <- this was the commit for the day!!')

        os.system('git add data.txt')

        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

        return days * makeCommits(days - 1)

makeCommits (4)