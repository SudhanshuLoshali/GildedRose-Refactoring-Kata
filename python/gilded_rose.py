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
            if item.name == self.AGED_BRIE:
                self._update_aged_brie(item)
            elif item.name == self.BACKSTAGE_PASSES:
                self._update_backstage_passes(item)
            elif item.name == self.SULFURAS:
                pass  # Sulfuras never changes
            elif self.CONJURED_PREFIX in item.name:
                self._update_conjured_item(item)
            else:
                self._update_normal_item(item)

    def _update_normal_item(self, item):
        """Update quality and sell-in for normal items."""
        if item.quality > self.MIN_QUALITY:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > self.MIN_QUALITY:
            item.quality -= 1

    def _update_aged_brie(self, item):
        """Update quality and sell-in for Aged Brie."""
        if item.quality < self.MAX_QUALITY:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < self.MAX_QUALITY:
            item.quality += 1

    def _update_backstage_passes(self, item):
        """Update quality and sell-in for Backstage Passes."""
        if item.quality < self.MAX_QUALITY:
            item.quality += 1
            if item.sell_in < 11 and item.quality < self.MAX_QUALITY:
                item.quality += 1
            if item.sell_in < 6 and item.quality < self.MAX_QUALITY:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = self.MIN_QUALITY

    def _update_conjured_item(self, item):
        """Update quality and sell-in for Conjured items (degrade twice as fast)."""
        if item.quality > self.MIN_QUALITY:
            item.quality -= 2 if item.quality >= 2 else item.quality
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > self.MIN_QUALITY:
            item.quality -= 2 if item.quality >= 2 else item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
