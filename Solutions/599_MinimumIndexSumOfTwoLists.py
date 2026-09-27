list1_1, list1_2 = ["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
list2_1, list2_2 = ["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]
list3_1, list3_2 = ["happy","sad","good"], ["sad","happy","good"]

def sol(list1, list2):
    freq = {}

    for i in range(len(list2)):
        freq[list2[i]] = i

    ans = []
    min = float("inf")

    for i in range(len(list1)):
        if list1[i] in freq:
            total = i + freq[list1[i]]

            if total < min:
                min = total
                ans = [list1[i]]
            elif total == min:
                ans.append(list1[i])

    return ans

print(sol(list1_1, list1_2))
print(sol(list2_1, list2_2))
print(sol(list3_1, list3_2))