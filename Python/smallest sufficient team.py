def smallestSufficientTeam(req_skills, people):
    n = len(req_skills)
    index = {skill: i for i, skill in enumerate(req_skills)}
    dp = {0: []}

    for i, j in enumerate(people):
        peopleSkill = 0
        for skill in j:
            peopleSkill |= (1 << index[skill])  # converting to binary.

        for preSkill, team in list(dp.items()):
            update = peopleSkill | preSkill

            if update == preSkill:
                continue

            if update not in dp or len(dp[update]) > len(team) + 1:
                dp[update] = team + [i]

    return dp[(1 << n)-1]


print(smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"], people=[
      ["java"], ["nodejs"], ["nodejs", "reactjs"]]))
