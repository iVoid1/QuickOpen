from flask import Flask, request, jsonify
from quickopen.core.logger import log


class Server:
    def __init__(self, command_handler):
        self.command_handler = command_handler
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/commands", methods=["GET"])
        def get_commands():
            return jsonify(self.command_handler.command_config.config)

        @self.app.route("/", methods=["POST"])
        def add_command():
            data = request.get_json()
            shortcut = data.get("shortcut")
            command = data.get("command")

            if not shortcut or not command:
                return jsonify({"error": "Missing shortcut or command"}), 400

            success = self.command_handler.add_command(shortcut, command)
            if success:
                return jsonify(self.command_handler.command_config.config)

            return jsonify({"error": "Failed to add command"}), 400

        @self.app.route("/<shortcut>", methods=["DELETE"])
        def remove_command(shortcut):
            index = self.command_handler.command_config.index_config(shortcut)
            if index is not None:
                success = self.command_handler.remove_command(index)
                if success:
                    return jsonify(self.command_handler.command_config.config)
            return jsonify({"error": "command not found"}), 404

    def run(self):
        self.app.run(host="0.0.0.0", port=3000)
