class ChemicalElement:  # Element name, Symbol, Atomic Number, Mass Number, Family, Metal/Metalloid/Nonmetal
    def __init__(self, name: str, sym: str, aNum: int, group: int, per: int, mNum, fam, clsf):
        self.name: str = name
        self.symbol: str = sym
        self.atomic_num: int = aNum
        self.group: int = group
        self.period: int = per
        self.mass_number: float = mNum
        self.family: str = fam
        self.classification: str = clsf

    def get_details(self):
        return {
            "element-name": self.name,
            "symbol": self.symbol,
            "atomic-number": self.atomic_num,
            "group": self.group,
            "period": self.period,
            "mass-number": self.mass_number,
            "family": self.family,
            "classification": self.classification
        }


# element = (name, symbol, atomic number, group, period, mass number,
# family, classification{metal, nonmetal, metalloid})
hydrogen = ChemicalElement('Hydrogen', 'H', 1, 1, 1, 1.008, 'Reactive Nonmetals', 'Nonmetal')
lithium = ChemicalElement('Lithium', 'O', 3, 1, 2, 6.94, 'Alkali Metals', 'Metal')
sodium = ChemicalElement('Sodium', 'Na', 11, 1, 3, 22.990, 'Alkali Metals', 'Metal')
potassium = ChemicalElement('Potassium', 'K', 19, 1, 4, 39.098, 'Alkali Metals', 'Metal')
rubidium = ChemicalElement('Rubidium', 'Rb', 37, 1, 5, 85.460, 'Alkali Metals', 'Metal')
caesium = ChemicalElement('Caesium', 'Cs', 55, 1, 6, 132.91, 'Alkali Metals', 'Metal')
francium = ChemicalElement('Francium', 'Fr', 87, 1, 7, 223.0, 'Alkali Metals', 'Metal')
# ^^^^^  Group One (Alkali Metals)  ^^^^^
beryllium = ChemicalElement('Beryllium', 'Be', 4, 2, 2, 9.0122, 'Alkaline Earth Metals', 'Metal')
magnesium = ChemicalElement('Magnesium', 'Mg', 12, 2, 3, 24.305, 'Alkaline Earth Metals', 'Metal')
calcium = ChemicalElement('Calcium', 'Ca', 20, 2, 4, 40.078, 'Alkaline Earth Metals', 'Metal')
strontium = ChemicalElement('Strontium', 'Sr', 38, 2, 5, 87.62, 'Alkaline Earth Metals', 'Metal')
barium = ChemicalElement('Barium', 'Ba', 56, 2, 6, 137.33, 'Alkaline Earth Metals', 'Metal')
radium = ChemicalElement('Radium', 'Ra', 88, 2, 7, 226, 'Alkaline Earth Metals', 'Metal')
# ^^^^ Group Two (Alkaline Earth Metals) ^^^^
scandium = ChemicalElement('Scandium', 'Sc', 21, 3, 4, 44.956, 'Transition Metals', 'Metal')
yttrium = ChemicalElement('Yttrium', 'Y', 39, 3, 4, 88.906, 'Transition Metals', 'Metal')
# vvvv  Lanthanoids  vvvv
element = ChemicalElement('X', '0', 57, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 58, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 59, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 60, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 61, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 62, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 63, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 64, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 65, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 66, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 67, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 68, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 69, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 70, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
element = ChemicalElement('X', '0', 71, 3, 2, 6.94, 'Transition Metals - Lanthanoids', 'Metal')
# vvvv  Actinides  vvvv
element = ChemicalElement('X', '0', 3, 1, 2, 6.94, 'Transition Metals', 'Metal')
element = ChemicalElement('X', '0', 3, 1, 2, 6.94, 'Transition Metals', 'Metal')
# ^^^^ Group Three - Twelve (Transition Metals) ^^^^
