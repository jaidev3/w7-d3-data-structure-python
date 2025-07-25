monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}

def unique_visitors_across_all_days(monday_visitors, tuesday_visitors, wednesday_visitors):
    all_unique_visitors = monday_visitors | tuesday_visitors | wednesday_visitors
    return all_unique_visitors

print("1. Unique visitors across all days:")
print(f"Users: {unique_visitors_across_all_days(monday_visitors, tuesday_visitors, wednesday_visitors)}")
print(f"Total count: {len(unique_visitors_across_all_days(monday_visitors, tuesday_visitors, wednesday_visitors))}")
print()

def returning_visitors_on_tuesday(monday_visitors, tuesday_visitors):
    returning_users = monday_visitors & tuesday_visitors
    return returning_users

print("2. Returning visitors on Tuesday (visited both Monday and Tuesday):")
print(f"Users: {returning_visitors_on_tuesday(monday_visitors, tuesday_visitors)}")
print(f"Count: {len(returning_visitors_on_tuesday(monday_visitors, tuesday_visitors))}")
print()

def new_visitors_each_day(monday_visitors, tuesday_visitors, wednesday_visitors):
    new_monday = monday_visitors  # All Monday visitors are new (first day)
    new_tuesday = tuesday_visitors - monday_visitors  # Tuesday visitors not seen on Monday
    new_wednesday = wednesday_visitors - monday_visitors - tuesday_visitors  # Wednesday visitors not seen before
    return new_monday, new_tuesday, new_wednesday

print("3. New visitors each day:")
new_mon, new_tue, new_wed = new_visitors_each_day(monday_visitors, tuesday_visitors, wednesday_visitors)
print(f"New on Monday: {new_mon}")
print(f"New on Tuesday: {new_tue}")
print(f"New on Wednesday: {new_wed}")
print()

def loyal_visitors(monday_visitors, tuesday_visitors, wednesday_visitors):
    loyal_users = monday_visitors & tuesday_visitors & wednesday_visitors
    return loyal_users

print("4. Loyal visitors (visited all three days):")
print(f"Users: {loyal_visitors(monday_visitors, tuesday_visitors, wednesday_visitors)}")
print(f"Count: {len(loyal_visitors(monday_visitors, tuesday_visitors, wednesday_visitors))}")
print()

def daily_visitor_overlap_analysis(monday_visitors, tuesday_visitors, wednesday_visitors):
    monday_tuesday = monday_visitors & tuesday_visitors
    tuesday_wednesday = tuesday_visitors & wednesday_visitors
    monday_wednesday = monday_visitors & wednesday_visitors
    return monday_tuesday, tuesday_wednesday, monday_wednesday

print("5. Daily visitor overlap analysis:")
mon_tue, tue_wed, mon_wed = daily_visitor_overlap_analysis(monday_visitors, tuesday_visitors, wednesday_visitors)
print(f"Monday-Tuesday overlap: {mon_tue}")
print(f"Tuesday-Wednesday overlap: {tue_wed}")
print(f"Monday-Wednesday overlap: {mon_wed}")