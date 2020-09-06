from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    # pass
    animal_type_list = ['eat_grass', 'eat_meat']  # 类型
    physique_list = ['S', 'M', 'L', 'XL']  # 体型
    disposition_list = ['Nice', 'Ferocious']  # 性格

    @abstractmethod
    def is_ferocious_animal(self, physique, disposition, animal_type):  # 是否凶猛
        ferocious_animal = False
        if physique >= 'M' and disposition is 'Ferocious' and animal_type is 'eat_meat':
            ferocious_animal = True
        return ferocious_animal

f