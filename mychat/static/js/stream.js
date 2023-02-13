const APP_ID = '5d57557d758b40ac914e803afd5dec41'
const CHANNEL_NAME = 'main'
const TOKEN = '0065d57557d758b40ac914e803afd5dec41IAAAKAlii6NSlEsFMkbwnDb7fnZqb32IcpHLbCGjXxmRd2TNKL8AAAAAEABptZ5ijTHaYgEAAQCMMdpi'

const client = AgoraRTC.createClient({mode:'rtc',codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {

    client.on('user-published', handleUserJoined)
    client.on('user-left', handleUserLeft)

    UID = await client.join(APP_ID, CHANNEL_NAME, TOKEN, null)

    localTracks =  await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = ` <div class="container video-container m-3" id="user-container-${UID}">
    <div class="username-wrapper"><span class="user-name">My name: </span></div>
    <div class="video-player" id="user-${UID}"></div>
</div> `

document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
localTracks[1].play(`user-${UID}`)
await client.publish([localTracks[0], localTracks[1]])
}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if((mediaType) === 'video'){
        let player = document.getElementById(`user-container-${user.uid}`)
        if(player!=null){
            player.remove()
        }

        player = ` <div class="container video-container m-3" id="user-container-${user.uid}">
        <div class="username-wrapper"><span class="user-name">My name: </span></div>
        <div class="video-player" id="user-${user.uid}"></div>
        </div> `
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

        user.videoTrack.play(`user-${user.uid}`)    
    }

    if(mediaType === 'audio'){
        user.audioTrack.play()
    }
}

let handleUserLeft = async(user) => {
    delete remoteUsers[user.uid]
    document.getElementById(`user-container-${user.uid}`).remove()
}

joinAndDisplayLocalStream()