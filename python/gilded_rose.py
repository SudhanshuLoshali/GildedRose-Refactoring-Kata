# -*- coding: utf-8 -*-

class GildedRose:
    """Manages a list of items and updates their quality and sell-in values daily."""

    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        """Initialize with a list of items."""
        self.items = items

    def update_quality(self):
        """Update quality and sell-in values for all items based on their type."""
        for item in self.items:
            if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASSES:
                if item.quality > 0:
                    if item.name != self.SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == self.BACKSTAGE_PASSES:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != self.SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != self.AGED_BRIE:
                    if item.name != self.BACKSTAGE_PASSES:
                        if item.quality > 0:
                            if item.name != self.SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
