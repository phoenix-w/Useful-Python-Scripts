import numpy as np
import pandas as pd

# calculate confidence {A} -> {B}
def confidence(A, B):
    """
    Calculate confidence {A} -> {B}.
    A and B are arrays that only contain boolean values.
    e.g. A=df["antecedent"], B=df["consequent"]
    """
    support_A = A.mean()
    support_AB = np.logical_and(A, B).mean()
    return support_AB/support_A


# calculate lift {A} -> {B}
def lift(A, B):
    """
    Calculate lift {A} -> {B}.
    A and B are arrays that only contain boolean values.
    e.g. A=df["antecedent"], B=df["consequent"]
    """
    support_A = A.mean()
    support_B = B.mean()
    support_AB = np.logical_and(A, B).mean()
    return support_AB / (support_A*support_B)


# calculate leverage {A} -> {B}
def leverage(A, B):
    """
    Calculate leverage {A} -> {B}.
    A and B are arrays that only contain boolean values.
    e.g. A=df["antecedent"], B=df["consequent"]
    """
    support_A = A.mean()
    support_B = B.mean()
    support_AB = np.logical_and(A, B).mean()
    return support_AB - support_A*support_B


# calculate conviction {A} -> {B}
def conviction(A, B):
    """
    Calculate conviction {A} -> {B}.
    A and B are arrays that only contain boolean values.
    e.g. A=df["antecedent"], B=df["consequent"]
    """
    support_AB = np.logical_and(A, B).mean()
    support_A = A.mean()
    support_notB = 1.0 - B.mean()
    support_AnotB = support_A - support_AB
    return (support_A*support_notB) / support_AnotB


# calculate Zhang's metric {A} -> {B}
def zhang(A, B):
    """
    Calculate Zhang's metric {A} -> {B}.
    A and B are arrays that only contain boolean values.
    e.g. A=df["antecedent"], B=df["consequent"]
    """
    support_A = A.mean()
    support_B = B.mean()
    support_AB = np.logical_and(A, B).mean()
    numerator = support_AB - support_A*support_B
    denominator = max( support_AB*(1-support_A) , support_A*(support_B-support_AB) )
    return numerator/denominator