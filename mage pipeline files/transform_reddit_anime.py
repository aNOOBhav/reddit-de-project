if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(df, *args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block (if applicable)
        args: The output from any additional upstream blocks

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    #create topic
    df.loc[df['thread'].str.contains("Episode"),'Topic'] = 'Episode'
    df.loc[df['thread'].str.contains("visual"),'Topic'] = 'Visual'
    df.loc[df['thread'].str.contains("Visual"),'Topic'] = 'Visual'
    df.loc[df['thread'].str.contains("Announced"),'Topic'] = 'Announcements'
    df.loc[df['thread'].str.contains("announced"),'Topic'] = 'Announcements'

    #create anime name logic
    df.loc[df['thread'].str.contains("Suzume"),'Anime'] = 'Suzume'
    df.loc[df['thread'].str.contains("Kimetsu"),'Anime'] = 'Demon Slayer'
    df.loc[df['thread'].str.contains("Oshi"),'Anime'] = 'Oshi no Ko'
    df.loc[df['thread'].str.contains("Chainsaw"),'Anime'] = 'Chainsaw Man'
    df.loc[df['thread'].str.contains("Jujutsu"),'Anime'] = 'Jujutsu Kaisen'
    df.loc[df['thread'].str.contains("JUJUTSU"),'Anime'] = 'Jujutsu Kaisen'
    df.loc[df['thread'].str.contains("One Punch"),'Anime'] = 'One Punch Man'
    df.loc[df['thread'].str.contains("Naruto"),'Anime'] = 'Naruto'
    df.loc[df['thread'].str.contains("Dragon Ball"),'Anime'] = 'Dragon Ball'
    df.loc[df['thread'].str.contains("SPY"),'Anime'] = 'SPY X Family'
    df.loc[df['thread'].str.contains("Spy"),'Anime'] = 'SPY X Family'
    df.loc[df['thread'].str.contains("Attack"),'Anime'] = 'Attack on Titan'
    df.loc[df['thread'].str.contains("ATTACK"),'Anime'] = 'Attack on Titan'
    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
