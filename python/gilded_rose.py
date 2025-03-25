# -*- coding: utf-8 -*-

class GildedRose:
    """Manages a list of items and updates their quality and sell-in values daily."""

    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    CONJURED_PREFIX = "Conjured"
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        """Initialize with a list of items."""
        self.items = items

    def update_quality(self):
        """Update quality and sell-in values for all items based on their type."""
        for item in self.items:
            updater = self._get_updater(item)
            updater.update()

    def _get_updater(self, item):
        if item.name == self.AGED_BRIE:
            return AgedBrieUpdater(item)
        elif item.name == self.BACKSTAGE_PASSES:
            return BackstagePassUpdater(item)
        elif item.name == self.SULFURAS:
            return SulfurasUpdater(item)
        elif self.CONJURED_PREFIX in item.name:
            return ConjuredItemUpdater(item)
        else:
            return ItemUpdater(item)

class ItemUpdater:
    """Base updater for normal items."""
    def __init__(self, item):
        self.item = item
        self.MAX_QUALITY = GildedRose.MAX_QUALITY
        self.MIN_QUALITY = GildedRose.MIN_QUALITY

    def update(self):
        """Update quality and sell-in for normal items."""
        if self.item.quality > self.MIN_QUALITY:
            self.item.quality -= 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality > self.MIN_QUALITY:
            self.item.quality -= 1

class AgedBrieUpdater(ItemUpdater):
    """Updater for Aged Brie items."""
    def update(self):
        if self.item.quality < self.MAX_QUALITY:
            self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality < self.MAX_QUALITY:
            self.item.quality += 1

class BackstagePassUpdater(ItemUpdater):
    """Updater for Backstage Passes."""
    def update(self):
        if self.item.quality < self.MAX_QUALITY:
            self.item.quality += 1
            if self.item.sell_in < 11 and self.item.quality < self.MAX_QUALITY:
                self.item.quality += 1
            if self.item.sell_in < 6 and self.item.quality < self.MAX_QUALITY:
                self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = self.MIN_QUALITY

class SulfurasUpdater(ItemUpdater):
    """Updater for Sulfuras (no changes)."""
    def update(self):
        pass

class ConjuredItemUpdater(ItemUpdater):
    """Updater for Conjured items (degrade twice as fast)."""
    def update(self):
        if self.item.quality > self.MIN_QUALITY:
            self.item.quality = max(self.MIN_QUALITY, self.item.quality - 2)
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality > self.MIN_QUALITY:
            self.item.quality = max(self.MIN_QUALITY, self.item.quality - 2)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
