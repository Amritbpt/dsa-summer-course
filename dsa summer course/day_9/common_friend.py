alice_friends={'Bob', 'Carol', 'Dave', 'Eve'}
bob_friends={'Alice', 'Carol', 'Frank', 'Dave'}
common_friend=alice_friends & bob_friends
alice_exclusive=alice_friends - bob_friends
unique = alice_friends | bob_friends
print(f"commom friends : {common_friend}, alice exclusive friends : {alice_exclusive}, unique peoples : {len(unique)}, {unique}")