from typing import Dict, Any

class ProfessionalResponsePipeline:
    def inlet(self, body: Dict[str, Any]) -> Dict[str, Any]:
        system_prompt = (
            "You are a professional assistant. "
            "Keep responses clear, concise, and well-structured."
        )

        messages = body.get("messages", [])
        messages.insert(0, {"role": "system", "content": system_prompt})
        body["messages"] = messages

        return body

    def outlet(self, body: Dict[str, Any]) -> Dict[str, Any]:
        if "choices" in body:
            for choice in body["choices"]:
                choice["message"]["content"] += "\n\n— Response refined by custom pipeline"
        return body





