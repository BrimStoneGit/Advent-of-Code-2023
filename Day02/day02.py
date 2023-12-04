import pandas as pd
import re

index_levels = ['Game', 'Draw']

def part1():
    # Read in Input
    with open('Day02/Input.txt') as f:
        lines = f.readlines()
    # Set up DataFrame
    result_df = pd.DataFrame()
    # Format the "Game" column
    lines = [x.replace("Game ", "") for x in lines]
    lines = [x.replace(": ", "; ") for x in lines]
    df_data = []
    for line in lines:
        for round in line.split("; ")[1:]:
            # write out RGB values
            data = [
                regex_resolve(r'(\d+) red', round), 
                regex_resolve(r'(\d+) green', round), 
                regex_resolve(r'(\d+) blue', round), 
            ]
            df_data.append(data)
        multi_index = pd.MultiIndex.from_product([[int(line.split(";")[0])],[*range(len(line.split("; ")) - 1)]], names=index_levels)
        # Create DataFrame with the Multiindex of "game" and "draw"
        df = pd.DataFrame(df_data, index=multi_index)
        if result_df.empty:
            # Init DataFrame
            result_df = df
        else:
            # Append DataFrame
            frames = [result_df, df]
            result_df = pd.concat(frames)
        df_data = []
    sum = 0
    for game, game_df in result_df.groupby(level=0):
        # Check if game is valid
        if game_df[0].max() <= 12 and game_df[1].max() <= 13 and game_df[2].max() <= 14:
            sum += game
    print(sum)
    

def regex_resolve(regex: str, line: str) -> int:
    try:
        return int(re.findall(regex, line)[0])
    except IndexError:
        return 0

def part2():
    # Read in Input
    with open('Day02/Input.txt') as f:
        lines = f.readlines()
    # Set up DataFrame
    result_df = pd.DataFrame()
    # Format the "Game" column
    lines = [x.replace("Game ", "") for x in lines]
    lines = [x.replace(": ", "; ") for x in lines]
    df_data = []
    for line in lines:
        for round in line.split("; ")[1:]:
            # write out RGB values
            data = [
                regex_resolve(r'(\d+) red', round), 
                regex_resolve(r'(\d+) green', round), 
                regex_resolve(r'(\d+) blue', round), 
            ]
            df_data.append(data)
        multi_index = pd.MultiIndex.from_product([[int(line.split(";")[0])],[*range(len(line.split("; ")) - 1)]], names=index_levels)
        # Create DataFrame with the Multiindex of "game" and "draw"
        df = pd.DataFrame(df_data, index=multi_index)
        if result_df.empty:
            # Init DataFrame
            result_df = df
        else:
            # Append DataFrame
            frames = [result_df, df]
            result_df = pd.concat(frames)
        df_data = []
    sum = 0
    for game, game_df in result_df.groupby(level=0):
        # Get the max value of each color column and multiply it
        power = game_df[0].max() * game_df[1].max() * game_df[2].max()
        sum += power
    print(sum)

if __name__ == '__main__':
    part1()
    part2()