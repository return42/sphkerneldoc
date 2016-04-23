#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-

u"""
    flat-table
    ~~~~~~~~~~

    Implementation of the ``flat-table`` reST-directive.

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    Documentation TODO.

    The ``flat-table`` (:py:class:`FlatTable`) is a double-stage list similar
    to the ``list-table`` with some additional features:

    * *colunm-span*: with the role ``cspan`` a cell can be extended through
       additional columns

    * *row-span*: with the role ``rspan`` a cell can be extended through
       additional rows

    * Autospan last cell over missing cell on the right side of the table-row.
      With Option ``:fill-cells:`` this behavior can changed to insert empty
      cells instead of spanning.

    Options:

    * \:header-rows:   [int] count of header rows
    * \:stub-columns:  [int] count of stub columns
    * \:widths:        [[int] [int] ... ] widths of columns
    * \:fill-cells:    instead of autospann missing cells, insert missing cells

    roles:

    * \:cspan: [int] additionale columns (*morecols*)
    * \:rspan: [int] additionale rows (*morerows*)
"""

# ==============================================================================
# imports
# ==============================================================================

from docutils import io, nodes, statemachine, utils
from docutils.parsers.rst import directives, roles
from docutils.parsers.rst.directives.tables import Table
from docutils.utils import SystemMessagePropagation

# ==============================================================================
def init():
# ==============================================================================

    directives.register_directive("flat-table", FlatTable)
    roles.register_local_role('cspan', cspan)
    roles.register_local_role('rspan', rspan)

# ==============================================================================
def cspan(name, rawtext, text, lineno, inliner, options=None, content=None):
# ==============================================================================

    options  = options if options is not None else {}
    content  = content if content is not None else []
    nodelist = [colSpan(span=int(text))]
    msglist  = []
    return nodelist, msglist

# ==============================================================================
def rspan(name, rawtext, text, lineno, inliner, options=None, content=None):
# ==============================================================================

    options  = options if options is not None else {}
    content  = content if content is not None else []
    nodelist = [rowSpan(span=int(text))]
    msglist  = []
    return nodelist, msglist


# ==============================================================================
class rowSpan(nodes.General, nodes.Element): pass
class colSpan(nodes.General, nodes.Element): pass
# ==============================================================================

# ==============================================================================
class FlatTable(Table):
# ==============================================================================

    u"""FlatTable (``flat-table``) directive"""

    has_content = True
    required_arguments = 0
    optional_arguments = 1   # the title of the table
    final_argument_whitespace = False

    option_spec = {
        'name': directives.unchanged
        , 'class': directives.class_option
        , 'header-rows': directives.nonnegative_int
        , 'stub-columns': directives.nonnegative_int
        , 'widths': directives.positive_int_list
        , 'fill-cells' : directives.flag }

    def run(self):

        if not self.content:
            error = self.state_machine.reporter.error(
                'The "%s" directive is empty; content required.' % self.name,
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return [error]

        title, messages = self.make_title()
        node = nodes.Element()          # anonymous container for parsing
        self.state.nested_parse(self.content, self.content_offset, node)

        tableBuilder = ListTableBuilder(self)
        tableBuilder.parseFlatTableNode(node)
        tableNode = tableBuilder.buildTableNode()
        # SDK.CONSOLE()  # print --> tableNode.asdom().toprettyxml()
        return [tableNode]


# ==============================================================================
class ListTableBuilder(object):
# ==============================================================================

    u"""Builds a table from a double-stage list"""

    def __init__(self, directive):
        self.directive = directive
        self.rows      = []
        self.max_cols  = 0

    def buildTableNode(self):

        colwidths    = self.directive.get_column_widths(self.max_cols)
        stub_columns = self.directive.options.get('stub-columns', 0)
        header_rows  = self.directive.options.get('header-rows', 0)

        table = nodes.table()
        tgroup = nodes.tgroup(cols=len(colwidths))
        table += tgroup


        for colwidth in colwidths:
            colspec = nodes.colspec(colwidth=colwidth)
            # FIXME: It seems, that the stub method only works well in the
            # absence of rowspan (observed by the html builer, the docutils-xml
            # build seems OK).  This is not extraordinary, because there exists
            # no table directive (except *this* flat-table) which allows to
            # define coexistent of rowspan and stubs (there was no use-case
            # before flat-table). This should be reviewed (later).
            if stub_columns:
                colspec.attributes['stub'] = 1
                stub_columns -= 1
            tgroup += colspec
        stub_columns = self.directive.options.get('stub-columns', 0)

        if header_rows:
            thead = nodes.thead()
            tgroup += thead
            for row in self.rows[:header_rows]:
                thead += self.buildTableRowNode(row)

        tbody = nodes.tbody()
        tgroup += tbody

        for row in self.rows[header_rows:]:
            tbody += self.buildTableRowNode(row)
        return table

    def buildTableRowNode(self, row_data, classes=None):
        classes = [] if classes is None else classes
        row = nodes.row()
        for cell in row_data:
            if cell is None:
                continue
            cspan, rspan, cellElements = cell

            attributes = {"classes" : classes}
            if rspan:
                attributes['morerows'] = rspan
            if cspan:
                attributes['morecols'] = cspan
            entry = nodes.entry(**attributes)
            entry.extend(cellElements)
            row += entry
        return row

    def raiseError(self, msg):
        error =  self.directive.state_machine.reporter.error(
            msg
            , nodes.literal_block(self.directive.block_text
                                  , self.directive.block_text)
            , line = self.directive.lineno )
        raise SystemMessagePropagation(error)

    def parseFlatTableNode(self, node):
        u"""parses the node from a :py:class:`FlatTable` directive's body"""

        if len(node) != 1 or not isinstance(node[0], nodes.bullet_list):
            self.raiseError(
                'Error parsing content block for the "%s" directive: '
                'exactly one bullet list expected.' % self.directive.name )

        for rowNum, rowItem in enumerate(node[0]):
            row = self.parseRowItem(rowItem, rowNum)
            self.rows.append(row)
        self.roundOffTableDefinition()

    def roundOffTableDefinition(self):
        u"""Round off the table definition.

        This method rounds off the table definition in :py:member:`rows`.

        * This method inserts the needed ``None`` values for the missing cells
        arising from spanning cells over rows and/or columns.

        * recount the :py:member:`max_cols`

        * Autospan or fill (option ``fill-cells``) missing cells on the right
          side of the table-row
        """

        y = 0
        while y < len(self.rows):
            x = 0

            while x < len(self.rows[y]):
                cell = self.rows[y][x]
                if cell is None:
                    x += 1
                    continue
                cspan, rspan = cell[:2]
                # handle colspan in current row
                for c in range(cspan):
                    self.rows[y].insert(x+c+1, None)
                # handle colspan in spnned rows
                for r in range(rspan):
                    for c in range(cspan + 1):
                        self.rows[y+r+1].insert(x+c, None)
                x += 1
            y += 1

        # Insert the missing cells on the right side. For this, first
        # re-calculate the max columns.

        for row in self.rows:
            if self.max_cols < len(row):
                self.max_cols = len(row)

        # fill with empty cells or cellspan?

        fill_cells = False
        if 'fill-cells' in self.directive.options:
            fill_cells = True

        for row in self.rows:
            x =  self.max_cols - len(row)
            if x and not fill_cells:
                if row[-1] is None:
                    row.append( ( x - 1, 0, []) )
                else:
                    cspan, rspan, content = row[-1]
                    row[-1] = (cspan + x, rspan, content)
            elif x and fill_cells:
                for i in range(x):
                    row.append( (0, 0, nodes.comment()) )

    def pprint(self):
        # for debugging
        retVal = "[   "
        for row in self.rows:
            retVal += "[ "
            for col in row:
                if col is None:
                    retVal += ('%r' % col)
                    retVal += "\n    , "
                else:
                    content = col[2][0].astext()
                    if 30 < len (content):
                        content = content[:30] + "..."
                    retVal += ('(cspan=%s, rspan=%s, %r)'
                               % (col[0], col[1], content))
                    retVal += "]\n    , "
            retVal = retVal[:-2]
            retVal += "]\n  , "
        retVal = retVal[:-2]
        return retVal + "]"

    def parseRowItem(self, rowItem, rowNum):
        row = []
        if len(rowItem) != 1 or not isinstance(rowItem[0], nodes.bullet_list):
            self.raiseError(
                'Error parsing content block for the "%s" directive: '
                'two-level bullet list expected, but row %s does not '
                'contain a second-level bullet list.'
                % (self.directive.name, rowNum + 1))
        for cellItem in rowItem[0]:
            cspan, rspan, cellElements = self.parseCellItem(cellItem)
            row.append( (cspan, rspan, cellElements) )
        return row

    def parseCellItem(self, cellItem):
        # search and remove cspan, rspan colspec from the first element in
        # this listItem (field).
        cspan = rspan = 0
        for elem in cellItem[0]:
            if isinstance(elem, colSpan):
                cspan = elem.get("span")
                elem.parent.remove(elem)
                continue
            if isinstance(elem, rowSpan):
                rspan = elem.get("span")
                elem.parent.remove(elem)
                continue
        return cspan, rspan, cellItem[:]

# ==============================================================================
# init
# ==============================================================================

init()
