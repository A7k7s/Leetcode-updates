# Last updated: 7/14/2026, 2:02:19 PM
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        # Step 1: Sort scores in descending order
        sorted_score = sorted(score, reverse=True)

        # Step 2: Medal names
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        # Step 3: Map score → rank
        rank_mapping = {
            score: medals[i] if i < 3 else str(i + 1)
            for i, score in enumerate(sorted_score)
        }

        # Step 4: Return ranks in original order
        return [rank_mapping[score] for score in score]