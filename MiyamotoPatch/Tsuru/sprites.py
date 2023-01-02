# Tsuru
# Custom Miyamoto sprites.py Module
# Sprites Images


from PyQt5 import QtCore, QtGui
Qt = QtCore.Qt

import spritelib as SLib

ImageCache = SLib.ImageCache


class SpriteImage_ActorSpawner(SLib.SpriteImage_Static):  # 724
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['actor'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('actor', 'Actor_Spawner.png')


class SpriteImage_MassiveSpikedStake(SLib.SpriteImage_Static):  # 377
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['MassiveSpikedStake'],
            (-98, -2445),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('MassiveSpikedStake', 'massive_stake_down_e_0.png')


class SpriteImage_MortyMole(SLib.SpriteImage_Static):  # 692
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['mortymole'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('mortymole', 'mortymole.png')


class SpriteImage_Parabones(SLib.SpriteImage_Static):  # 725
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Parabones'],
            (0, -6),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Parabones', 'Parabones.png')

   
class SpriteImage_Cataquack(SLib.SpriteImage_Static):  # 733
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Cataquack'],
            (-10, -19),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Cataquack', 'cataquack.png')


class SpriteImage_RainbowLight(SLib.SpriteImage_Static):  # 738
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['RainbowLight'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('RainbowLight', 'light.png')


class SpriteImage_CustomDoor(SLib.SpriteImage_Static):  # 726
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['CustomDoor'],
            (-16, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CustomDoor', 'customdoor.png')


class SpriteImage_TimeClock(SLib.SpriteImage_Static):  # 734
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['TimeClock'],
            (-16, -16),
        )

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TimeClock', 'time_clock.png')

class SpriteImage_Scuttlebug(SLib.SpriteImage_Static):  # 749
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['scuttlebug'],
            (0, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('scuttlebug', 'scuttlebug.png')
    
class SpriteImage_Biddybud(SLib.SpriteImage_Static):  # 758
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Biddybud'],
            (-8, 0),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Biddybud', 'biddybud_red.png')
        
class SpriteImage_BasaltBones(SLib.SpriteImage_Static):  # 760
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['BasaltBones'],
            (-32, -40),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('BasaltBones', 'basaltbones.png')
        
class SpriteImage_Peepa(SLib.SpriteImage_StaticMultiple):  # 770 TODO: add different platform variations?
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
        )

        self.xOffset = 0

    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PeepaWoodPlat', 'peepa_platform.png')
        SLib.loadIfNotInImageCache('Peepa', 'peepa.png')
          
    def dataChanged(self):
        has_platform = (self.parent.spritedata[0] >> 1) & 8       
        
        if has_platform == 0:
            self.image = ImageCache['Peepa']
            
        elif has_platform == 8:
            self.image = ImageCache['PeepaWoodPlat']
            self.xOffset = -24
            

        super().dataChanged()


class SpriteImage_StarCoinShard(SLib.SpriteImage_Static):  # 729
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['StarCoinShard'],
            (-8, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('StarCoinShard', 'star_coin_shard.png')
        
class SpriteImage_Kamiya(SLib.SpriteImage_Static):  # 743
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Kamiya'],
            (-24, -32),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Kamiya', 'kamiya.png')
        
class SpriteImage_Chestnut(SLib.SpriteImage_Static):  # 731
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Chestnut'],
            (-8, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Chestnut', 'chestnut.png')
        
class SpriteImage_Flaptor(SLib.SpriteImage_Static):  # 761
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['Flaptor'],
            (-16, -8),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('Flaptor', 'flaptor.png')
        
class SpriteImage_ColdFuzzy(SLib.SpriteImage_Static):  # 753
    def __init__(self, parent):
        super().__init__(
            parent,
            3.75,
            ImageCache['ColdFuzzy'],
            (-16, -16),
        )

    def loadImages():
        SLib.loadIfNotInImageCache('ColdFuzzy', 'coldfuzzy.png')

       

ImageClasses = {
    724: SpriteImage_ActorSpawner,
    748: SpriteImage_MassiveSpikedStake,
    725: SpriteImage_Parabones,
    733: SpriteImage_Cataquack,
    738: SpriteImage_RainbowLight,
    726: SpriteImage_CustomDoor,
    734: SpriteImage_TimeClock,
    749: SpriteImage_Scuttlebug,
    758: SpriteImage_Biddybud,
    760: SpriteImage_BasaltBones,
    770: SpriteImage_Peepa,
    729: SpriteImage_StarCoinShard,
    743: SpriteImage_Kamiya,
    731: SpriteImage_Chestnut,
    761: SpriteImage_Flaptor,
    753: SpriteImage_ColdFuzzy
}
