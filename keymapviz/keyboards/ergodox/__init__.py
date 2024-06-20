# -*- coding: utf-8 -*-

keymap_keyword = '(?:LAYOUT_ergodox|KEYMAP|KEYMAP_80|LAYOUT_ergodox_pretty|KEYMAP_TKG)'
layout_editor_json = {
  'default': 'keyboards/ergodox/layout_editor/default.json',
  'plain': 'keyboards/ergodox/layout_editor/plain.json',
}

ascii_art = {
  'default': '''
/* .---------------------------------------------. .---------------------------------------------.
 * |{0    }|{1  }|{2  }|{3  }|{4  }|{5  }|{6    }| !{7    }|{8  }|{9  }|{10 }|{11 }|{12 }|{13   }|
 * !-------+-----+-----+-----+-----+-------------! !-------+-----+-----+-----+-----+-----+-------!
 * |{14   }|{15 }|{16 }|{17 }|{18 }|{19 }|{20   }| !{21   }|{22 }|{23 }|{24 }|{25 }|{26 }|{27   }|
 * !-------+-----+-----+-----x-----x-----!       ! !       !-----x-----x-----+-----+-----+-------!
 * |{28   }|{29 }|{30 }|{31 }|{32 }|{33 }|-------! !-------!{34 }|{35 }|{36 }|{37 }|{38 }|{39   }|
 * !-------+-----+-----+-----x-----x-----!{46   }! !{47   }!-----x-----x-----+-----+-----+-------!
 * |{40   }|{41 }|{42 }|{43 }|{44 }|{45 }|       | !       |{48 }|{49 }|{50 }|{51 }|{52 }|{53   }|
 * '-------+-----+-----+-----+-----+-------------' '-------------+-----+-----+-----+-----+-------'
 *  |{54  }|{55 }|{56 }|{57 }|{58 }|                             !{59 }|{60 }|{61 }|{62 }|{63  }|
 *  '------------------------------'                             '------------------------------'
 *                               .---------------. .---------------.
 *                               |{64   }|{65   }| !{66   }|{67   }|
 *                       .-------+-------+-------! !-------+-------+-------.
 *                       !{70   }!{71   }|{68   }| !{69   }|{74   }!{75   }!
 *                       !       !       !-------! !-------!       !       !
 *                       |       |       |{72   }| !{73   }|       |       |
 *                       '-----------------------' '-----------------------'
 *                                                  generated by [keymapviz] */
''',
  'plain': '''
/* .---------------------------------------------------.         .---------------------------------------------------.
 * |{0     }|{1   }|{2   }|{3   }|{4   }|{5   }|{6    }|         |{38   }|{39  }|{40  }|{41  }|{42  }|{43  }|{44    }|
 * |--------+------+------+------+------+--------------|         |-------+------+------+------+------+------+--------|
 * |{7     }|{8   }|{9   }|{10  }|{11  }|{12  }|{13   }|         |{45   }|{46  }|{47  }|{48  }|{49  }|{50  }|{51    }|
 * |--------+------+------+------x------x------|       |         |       |------x------x------+------+------+--------|
 * |{14    }|{15  }|{16  }|{17  }|{18  }|{19  }|-------|         |-------|{52  }|{53  }|{54  }|{55  }|{56  }|{57    }|
 * |--------+------+------+------x------x------|{26   }|         |{58   }|------x------x------+------+------+--------|
 * |{20    }|{21  }|{22  }|{23  }|{24  }|{25  }|       |         |       |{59  }|{60  }|{61  }|{62  }|{63  }|{64    }|
 * '--------+------+------+------+------+--------------'         '--------------+------+------+------+------+--------'
 *  |{27   }|{28  }|{29  }|{30  }|{31  }|                                       |{65  }|{66  }|{67  }|{68  }|{69   }|
 *  '-----------------------------------'                                       '-----------------------------------'
 *                                         .---------------. .---------------.
 *                                         |{32   }|{33   }| |{70   }|{71   }|
 *                                 .-------+-------+-------| |-------+-------+-------.
 *                                 |       |       |{34   }| |{72   }|       |       |
 *                                 |{35   }|{36   }|-------| |-------|{74   }|{75   }|
 *                                 |       |       |{37   }| |{73   }|       |       |
 *                                 '-----------------------' '-----------------------'
 *                                                                                     generated by [keymapviz] */
''',
}
