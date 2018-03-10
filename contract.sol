
/*
 * The actual smart contract that can store a message, an image and tags for each user
 */
contract ImgStorage
{
	// data structure to contain message, image and tags
	struct UserState
	{
        string userMessage;
        bytes userImage;
        string userTags;
	}
	
	// create a mapping from account-address to UserState,
	// this way, each user can store his own state,
	// the history is within the blockchain and can be retrieved as well
	// --> nothing lost
	mapping (address => UserState) userMapping;

	// now just some functions to actually set a new state and request it
	function getOwnUserState() constant returns(string, bytes, string)
	{
	    return getUserState(msg.sender);
	}

	function getUserState(address target) constant returns(string, bytes, string)
	{
        return (userMapping[target].userMessage,
                userMapping[target].userImage,
                userMapping[target].userTags);
	}

	function setNewUserState(string message, bytes imgData, string tags)
	{
		userMapping[msg.sender].userMessage = message;
		userMapping[msg.sender].userImage = imgData;
		userMapping[msg.sender].userTags = tags;
	}
}
