import React, { useState } from "react"; import { View, Text, TextInput, Button, ScrollView } from "react-native";

export default function App() { const [message, setMessage] = useState(""); const [response, setResponse] = useState(null);

const sendMessage = async () => { try { const res = await fetch("http://127.0.0.1:5000/api/query", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ message, language: "en", user_id: "demo" }), }); const data = await res.json(); setResponse(data); } catch (e) { setResponse({ error: "Server not reachable. Make sure Flask app is running." }); } };

const callAmbulance = async () => { try { const res = await fetch("http://127.0.0.1:5000/api/call_ambulance", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ lat: "28.7041", lon: "77.1025", user_id: "demo" }), }); const data = await res.json(); setResponse(data); } catch (e) { setResponse({ error: "Ambulance simulation failed." }); } };

return ( <View style={{ flex: 1, padding: 20, marginTop: 40 }}> <Text style={{ fontSize: 20, fontWeight: "bold", marginBottom: 10 }}> 🚑 Emergency Health Assistant </Text>

<TextInput
    placeholder="Describe the emergency..."
    value={message}
    onChangeText={setMessage}
    style={{ borderWidth: 1, padding: 10, marginBottom: 10 }}
  />

  <Button title="Send" onPress={sendMessage} />
  <View style={{ marginTop: 10 }} />
  <Button title="🚨 Call Ambulance (Simulated)" color="red" onPress={callAmbulance} />

  <ScrollView style={{ marginTop: 20, backgroundColor: "#f0f0f0", padding: 10, borderRadius: 8 }}>
    <Text style={{ fontSize: 16, fontWeight: "600" }}>Response:</Text>
    <Text selectable style={{ marginTop: 10 }}>
      {response ? JSON.stringify(response, null, 2) : "No response yet."}
    </Text>
  </ScrollView>
</View>

); 
}
