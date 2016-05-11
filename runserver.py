# -*- encoding: utf8 -*-

from core import app
import core.signals.listener

import fapp.context_processors
import fapp.views
import fapp.urls
import fapp.utils.auth
import fapp.templatetags




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=app.debug)
