#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# This file is part of SAMS.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

"""Superdesk Manager"""

import superdesk
from flask_script import Manager
from sams.factory.app import SamsApp

app = SamsApp()
manager = Manager(app)

if __name__ == '__main__':
    with app.app_context():
        manager.run(superdesk.COMMANDS)
