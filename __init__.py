from aqt import mw
from aqt import gui_hooks
# for gui debugging
from aqt.utils import showInfo, qconnect
from aqt.qt import *
import ast
from anki.cards import Card
from aqt.reviewer import Reviewer
from anki.notes import Note

def createVariation(reviewer: Reviewer, card: Card, ease: int) -> None:
    note = card.note()
    savePreviousVariation(note)

def savePreviousVariation(note: Note) -> None:
    updated_previous_variations = ast.literal_eval(note['Previous variations'])
    updated_previous_variations.append(note['Front'])
    note['Previous variations'] = str(updated_previous_variations)
    note.flush()

gui_hooks.reviewer_did_answer_card.append(createVariation)
