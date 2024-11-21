# Prep Material : Minimalistic Criteo API to understand Criteo's business model

# Advertiser: Clients who want to advertise the products
# Publisher :  Clients who offer their websites/platforms to publish ads
# Ad : A single advertisement / promotional content
# AdSlot : Banner where an add can be published
# Campaign : a campaign of ads
# CriteoInventory Class : Class managing all above components

import heapq
from collections import OrderedDict


class Advertiser:
    def __init__(self, id, name, campaigns=None, total_budget=None):
        self._id = id
        self.name = name
        self.campaigns = campaigns if campaigns is not None else {}
        self._total_budget = total_budget if total_budget is not None else 0

    def create_campaign(self, id, name, budget):
        if id in self.campaigns:
            raise Exception("Campaign already exists within the dict")

        campaign = Campaign(id, name, budget)
        self.campaigns[id] = campaign

    def get_active_campaigns(self):
        ans = []
        for idx, camp in self.campaigns.items():
            if camp.get_budget() > 0:
                ans.append(camp)
        return ans

    def deduct_spending(self, campaign_id, amount):
        if campaign_id not in self.campaigns:
            raise Exception("Campaign doesn't exist")
        elif self._total_budget < amount:
            raise Exception("Insufficient fund")
        camp = self.campaigns[campaign_id]
        camp.deduct_spending(amount)
        self._total_budget -= amount


class Campaign:
    def __init__(self, id, name, budget, ads=None, spent=None):
        self._id = id
        self.name = name
        self._budget = budget if budget is not None else 0
        self._ads = ads if ads is not None else {}
        self._spent = spent if spent is not None else 0

    def get_budget(self):
        return self._budget

    def set_budget(self, new_budget):
        self._budget = new_budget

    def deduct_spending(self, amount):
        if amount <= 0:
            raise ValueError("Amount is negative or null")
        self._budget -= amount

    def add_ad(self, ad):
        if ad._id not in self._ads:
            self._ads[ad._id] = ad
        else:
            raise Exception("Ad arleady exists")

    def get_ads(self):
        return self._ads.values()


class Ad:
    def __init__(self, id, campaign_id, amount, keywords=None):
        self._id = id
        self.campaign_id = campaign_id
        self._amount = amount
        self._nb_displays = 0
        self._clicks = 0
        self.keywords = keywords if keywords is not None else []

    def increment_clicks(self):
        self._clicks += 1

    def increment_nb_displays(self):
        self._nb_displays += 1

    def get_ctr(self):
        return self._clicks / self._nb_displays if self._nb_displays > 0 else 0


class AdSlot:
    def __init__(self, id, keywords, base_cost, publisher_id):
        self._id = id
        self.keywords = keywords
        self.base_cost = base_cost
        self.publisher_id = publisher_id
        self.current_ad = None

    def assign_ad(self, ad):
        self.current_ad = ad

    def clear_ad(self):
        self.current_ad = None


class LRUCache:
    """
    the intent of this class is to look up most recently
    published ads and either discard them either assign a low
    score for them in order to reselect the same ad multiple times.
    this ensures uniformity and balance when publising ads

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # remove LRU first inserted element
        self.cache[key] = value


class CriteoInventory:
    def __init__(self, ads_capacity=1000):
        self._ad_slots = []
        self._revenue = 0
        self.lru_cache = LRUCache(ads_capacity)

    def add_ad_slot(self, slot):
        self._ad_slots.append(slot)

    def match_ads(self, advertisers):
        for slot in self._ad_slots:
            max_heap = []
            for advertiser in advertisers:
                for campaign in advertiser.get_active_campaigns():
                    for ad in campaign.get_ads():
                        score = self.calculate_ad_score(ad, slot)
                        if ad._id in self.lru_cache:  # Uniformity
                            score = self.refine_score_on_nb_displays(score)
                        heapq.heappush(max_heap, (-score, ad, campaign, advertiser))
            if max_heap:
                _, selected_ad, campaign, advertiser = heapq.heappop(max_heap)
                slot.assign_ad(selected_ad)
                advertiser.deduct_spending(campaign._id, slot.base_cost)
                self._revenue += slot.base_cost
                self.lru_cache.put(selected_ad._id, selected_ad)

    def calculate_ad_score(self, ad, slot):
        relevance = sum([1 for keyword in ad.keywords if keyword in slot.keywords])
        ctr = ad.get_ctr()
        score = relevance * ctr * ad._amount
        return score

    def refine_score_on_nb_displays(self, score):
        # Apply logic to re adapt score if an ad is already published somewhere
        pass
