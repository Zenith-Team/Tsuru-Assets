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
            (-10, -19),
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


ImageClasses = {
    724: SpriteImage_ActorSpawner,
    748: SpriteImage_MassiveSpikedStake,
    725: SpriteImage_Parabones,
    733: SpriteImage_Cataquack,
    738: SpriteImage_RainbowLight,
    726: SpriteImage_CustomDoor,
    749: SpriteImage_Scuttlebug,
}
