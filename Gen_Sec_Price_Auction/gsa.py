"""
Generalized second-price auction
Source : https://en.wikipedia.org/wiki/Generalized_second-price_auction 
"""

bids_1 = {"a" : 20, "b" : 30, "c" : 10, "d" : 50}
bids_2 = {"a" : 1}
bids_3 = {}


def compare(bidder_1, bidder_2):
    """
    Input : tuple object
    """
    # bidder[0] => key, bidder[1] => value
    value = 1
    if bidder_1[value] == bidder_2[value]:
        return True
    else:
        return False

     
def calculate_auction(bids): 
    sorted_bids = sorted(bids.items(), reverse=True, key=lambda x:x[1])
    second_price_auction_bids = {}

    for i in range(len(sorted_bids)):
        key = 0
        value = 1

        is_equal = compare(sorted_bids[i], sorted_bids[i+1])
        
        if is_equal:
            """
            Validation if 2 Bids equal each other, should/shouldn't be happen?
            """
            pass
        else:
            second_price_auction_bids[(sorted_bids[i][key])] = sorted_bids[i+1][value]

        # last element : set it with "Lost the auction"
        if i == len(sorted_bids)-2:
            second_price_auction_bids[sorted_bids[i+1][key]] = "Lost the auction"
            break

    return second_price_auction_bids


def second_price_auction(bids):
    # case 1 : no bids
    if len(bids) == 0:
        return ("No Winners")
    
    # case 2 : only 1 bid
    if len(bids) == 1:
        # If there is only 1 Bid, then should return (Bid Floor + 0.01$)
        # But for this case will return the only sent Bid 
        return bids

    # case 3 : only 2 bids
    if len(bids) == 2:
        is_equal = compare(bids[0], bids[1])
        if is_equal:
            return bids
        else:
            bids = calculate_auction(bids)
            return bids

    # case 4 : more than 2 bids
    bids = calculate_auction(bids)
    return (bids)



if __name__ == "__main__":
    print ("Second price auction for many bids :", bids_1, " ===>", second_price_auction(bids_1))
    print ("Second price auction for 1 bid :", bids_2, "===>", second_price_auction(bids_2))
    print ("Second price auction for empty bids list :", bids_3, "===>", second_price_auction(bids_3))
